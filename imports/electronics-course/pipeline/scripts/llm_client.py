"""
LLM client for Qwen3.7 Plus via OpenCode Go (Anthropic-compatible API).
"""

import json
import time
import logging
import httpx
from config import (
    LLM_API_URL, LLM_MODEL, LLM_MAX_TOKENS,
    LLM_MAX_RETRIES, LLM_RETRY_DELAY
)


def _extract_text(response_json):
    """Extract text from Anthropic-style response, skipping thinking blocks."""
    content = response_json.get("content", [])
    if isinstance(content, str):
        return content
    for block in content:
        if isinstance(block, dict) and block.get("type") == "text":
            return block.get("text", "")
    raise KeyError(f"No 'text' block found in response content: {[b.get('type') for b in content if isinstance(b, dict)]}")


def call_llm(prompt: str, api_key: str, temperature: float = 0.3, system: str = None) -> str:
    """
    Call Qwen3.7 Plus via OpenCode Go API.
    """
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01"
    }
    
    messages = []
    if system:
        messages.append({"role": "user", "content": system})
        messages.append({"role": "assistant", "content": "I understand. I'll help with that."})
    
    messages.append({"role": "user", "content": prompt})
    
    payload = {
        "model": LLM_MODEL,
        "max_tokens": LLM_MAX_TOKENS,
        "temperature": temperature,
        "messages": messages,
        "thinking": {
            "type": "enabled",
            "budget_tokens": 1024
        }
    }
    
    for attempt in range(LLM_MAX_RETRIES):
        try:
            with httpx.Client(timeout=120.0) as client:
                response = client.post(LLM_API_URL, headers=headers, json=payload)
                response.raise_for_status()
                
                result = response.json()
                return _extract_text(result)
        
        except httpx.HTTPStatusError as e:
            is_retryable = e.response.status_code in [429, 500, 502, 503, 504]
            
            if is_retryable and attempt < LLM_MAX_RETRIES - 1:
                wait_time = LLM_RETRY_DELAY * (attempt + 1)
                logging.warning(f"Retryable error ({e.response.status_code}): {e}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                logging.error(f"HTTP error after {attempt + 1} attempts: {e}")
                raise
        
        except KeyError as e:
            logging.error(f"Response format error: {e}")
            if attempt < LLM_MAX_RETRIES - 1:
                time.sleep(LLM_RETRY_DELAY)
            else:
                raise
        
        except Exception as e:
            error_msg = str(e).lower()
            is_retryable = any(x in error_msg for x in ['timeout', 'connection', 'server'])
            
            if is_retryable and attempt < LLM_MAX_RETRIES - 1:
                wait_time = LLM_RETRY_DELAY * (attempt + 1)
                logging.warning(f"Retryable error: {e}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                logging.error(f"Failed after {attempt + 1} attempts: {e}")
                raise
    
    raise Exception("Max retries exceeded")


def call_llm_json(prompt: str, api_key: str, temperature: float = 0.3, system: str = None) -> dict:
    """
    Call LLM and parse JSON response.
    """
    response = call_llm(prompt, api_key, temperature, system)
    
    response = response.strip()
    
    # Remove markdown code blocks if present
    if response.startswith('```json'):
        response = response[7:]
    elif response.startswith('```'):
        response = response[3:]
    
    if response.endswith('```'):
        response = response[:-3]
    
    response = response.strip()
    
    try:
        return json.loads(response)
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse JSON: {e}")
        logging.error(f"Response was: {response[:500]}")
        raise

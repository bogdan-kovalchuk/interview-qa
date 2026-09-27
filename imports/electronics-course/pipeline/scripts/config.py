"""
Pipeline configuration - single source of truth.
"""

from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).resolve().parents[2]  # Course root
SUBTITLES_DIR = BASE_DIR / "subtitles"
OUTPUT_DIR = BASE_DIR / "pipeline" / "output"
LOGS_DIR = BASE_DIR / "pipeline" / "logs"

# PDF textbook path
PDF_PATH = BASE_DIR / "books" / "Design_Game_Console_013.pdf"

# Section configuration: ID -> (directory name, deck name)
SECTIONS = {
    "S01": ("Section 1 - The Starting Line", "The Starting Line"),
    "S02": ("Section 2 - Introduction to Electronics", "Introduction to Electronics"),
    "S03": ("Section 3 - Advanced Circuit Analysis Techniques and Tools", "Advanced Circuit Analysis"),
    "S04": ("Section 4 - Electrical Engineering 101 - And Here Comes the Crash Course Part...Buckle Up!", "Electrical Engineering 101"),
    "S05": ("Section 5 - Introduction to Digital Logic Systems, Boolean Algebra, Timing Diagrams and TTL", "Digital Logic Systems"),
    "S06": ("Section 6 - Taking Digital to the Next Level with Small, Medium, and Large Scale Integration", "Digital Scale Integration"),
    "S07": ("Section 7 - Printed Circuit Board Design and Technology with CircuitMaker", "PCB Design Technology"),
    "S08": ("Section 8 - Graduating to Design Engineer CircuitMaker Fundamentals and Real-World Projects", "CircuitMaker Projects"),
    "S09": ("Section 9 - Crash Course Bonus Lectures", "Bonus Lectures"),
}

# File naming conventions
def get_subtitle_chunks_path(section_id):
    """Per-section combined chunks file."""
    return OUTPUT_DIR / "subtitles" / f"{section_id}_chunks.json"

def get_subtitle_lecture_path(section_id, lecture_num):
    """Per-lecture chunks file."""
    return OUTPUT_DIR / "subtitles" / f"{section_id}_L{lecture_num:02d}.json"

def get_pdf_chunks_path():
    """PDF textbook chunks file."""
    return OUTPUT_DIR / "pdf" / "textbook_chunks.json"

def get_facts_path(section_id):
    """Extracted facts file for section."""
    return OUTPUT_DIR / "facts" / f"{section_id}_facts.json"

def get_cards_path(section_id):
    """Generated cards file for section."""
    return OUTPUT_DIR / "cards" / f"{section_id}_cards.txt"

def get_apkg_path(section_id):
    """Anki package file for section."""
    deck_name = SECTIONS[section_id][1].replace(" ", "_")
    return OUTPUT_DIR / "apkg" / f"{section_id}_{deck_name}.apkg"

# Anki configuration
ANKI_MODEL_ID = 1607392319
ANKI_MODEL_NAME = "Electronics Basic"

# LLM configuration - Qwen3.7 Plus via OpenCode Go
LLM_PROVIDER = "opencode_go"
LLM_MODEL = "qwen3.7-plus"
LLM_API_URL = "https://opencode.ai/zen/go/v1/messages"
LLM_MAX_TOKENS = 4096
LLM_TEMPERATURE_FACTS = 0.3
LLM_TEMPERATURE_CARDS = 0.5
LLM_MAX_RETRIES = 3
LLM_RETRY_DELAY = 5  # seconds

# Chunking configuration
MAX_CHUNK_WORDS = 800
MIN_CHUNK_WORDS = 100

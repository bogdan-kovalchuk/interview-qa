import { spawn } from 'node:child_process';
import { writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const siteRoot = fileURLToPath(new URL('../', import.meta.url));
const astroCli = fileURLToPath(new URL('../node_modules/astro/astro.js', import.meta.url));
const metricsFile = fileURLToPath(new URL('../.build-metrics.json', import.meta.url));
const started = performance.now();

const child = spawn(process.execPath, [astroCli, 'build'], {
  cwd: siteRoot,
  stdio: 'inherit',
});

child.on('error', (error) => {
  console.error(error);
  process.exitCode = 1;
});

child.on('close', async (code) => {
  const buildSeconds = (performance.now() - started) / 1000;
  await writeFile(
    metricsFile,
    JSON.stringify({ build_seconds: Number(buildSeconds.toFixed(3)), exit_code: code }, null, 2) + '\n',
    'utf8',
  );
  process.exitCode = code ?? 1;
});

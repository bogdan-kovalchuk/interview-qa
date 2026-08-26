// Production build entry point: mirror -> astro build.
//
// This is the single place that produces site/dist, and it is deliberately not
// possible to run `astro build` here without first regenerating the mirror from
// the current content/. site/src/content/docs is gitignored (it is generated),
// so nothing else guarantees it reflects the content on disk; a hand-run or
// stale `astro build` used to be able to ship yesterday's mirror. Content
// validation (`python -m iqa validate`) is a separate, cheaper, faster-failing
// step and runs before this script as part of the single `iqa build` pipeline
// (tools/iqa/build.py), which also runs `tools/verify_build.py` after this
// script succeeds - so the full path is validate -> mirror -> astro build ->
// verify, with exactly one command to invoke it.
import { spawn } from 'node:child_process';
import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const siteRoot = fileURLToPath(new URL('../', import.meta.url));
const repoRoot = fileURLToPath(new URL('../../', import.meta.url));
const astroCli = fileURLToPath(new URL('../node_modules/astro/astro.js', import.meta.url));
const metricsFile = path.join(siteRoot, '.build-metrics.json');

function run(command, args, options) {
  return new Promise((resolve) => {
    const child = spawn(command, args, { stdio: 'inherit', ...options });
    child.on('error', (error) => {
      console.error(error);
      resolve(1);
    });
    child.on('close', (code) => resolve(code ?? 1));
  });
}

async function writeMetrics(buildSeconds, exitCode) {
  await mkdir(path.dirname(metricsFile), { recursive: true });
  await writeFile(
    metricsFile,
    JSON.stringify({ build_seconds: Number(buildSeconds.toFixed(3)), exit_code: exitCode }, null, 2) + '\n',
    'utf8',
  );
}

const started = performance.now();

console.log('== 1/2: regenerate the production mirror ==');
const mirrorCode = await run(
  'python',
  [
    '-m',
    'iqa.mirror',
    '--root',
    repoRoot,
    '--source',
    path.join(repoRoot, 'content'),
    '--out',
    path.join(siteRoot, 'src', 'content', 'docs'),
    '--base',
    '/interview-qa',
  ],
  { cwd: repoRoot },
);
if (mirrorCode !== 0) {
  console.error('Mirror regeneration failed; refusing to run a production build on a stale mirror.');
  await writeMetrics((performance.now() - started) / 1000, mirrorCode);
  process.exitCode = mirrorCode;
  process.exit(mirrorCode);
}

console.log('== 2/2: astro build ==');
const astroCode = await run(process.execPath, [astroCli, 'build'], { cwd: siteRoot });
await writeMetrics((performance.now() - started) / 1000, astroCode);
process.exitCode = astroCode;

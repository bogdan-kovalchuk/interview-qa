// Build a disposable Starlight corpus to expose page-count scaling before the
// authored corpus reaches it. Nothing under content/ or site/src/ is touched.
import { spawn } from 'node:child_process';
import { mkdtemp, mkdir, readdir, rm, stat, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const siteRoot = fileURLToPath(new URL('../', import.meta.url));
const astroCli = fileURLToPath(new URL('../node_modules/astro/astro.js', import.meta.url));
const config = fileURLToPath(new URL('../astro.scale.config.mjs', import.meta.url));
const requested = Number.parseInt(process.argv[2] ?? '5000', 10);

if (!Number.isSafeInteger(requested) || requested < 2) {
  console.error('page count must be an integer of at least 2');
  process.exit(2);
}

function run(command, args, options) {
  return new Promise((resolve) => {
    const child = spawn(command, args, { stdio: ['ignore', 'ignore', 'inherit'], ...options });
    child.on('error', (error) => {
      console.error(error);
      resolve(1);
    });
    child.on('close', (code) => resolve(code ?? 1));
  });
}

async function treeMetrics(root) {
  let files = 0;
  let bytes = 0;
  let htmlPages = 0;
  const pending = [root];
  while (pending.length) {
    const directory = pending.pop();
    for (const entry of await readdir(directory, { withFileTypes: true })) {
      const target = path.join(directory, entry.name);
      if (entry.isDirectory()) {
        pending.push(target);
      } else if (entry.isFile()) {
        const { size } = await stat(target);
        files += 1;
        bytes += size;
        if (entry.name === 'index.html') htmlPages += 1;
      }
    }
  }
  return { files, bytes, htmlPages };
}

const temporary = await mkdtemp(path.join(siteRoot, '.scale-spike-'));
const source = path.join(temporary, 'src');
const docs = path.join(source, 'content', 'docs');
const output = path.join(temporary, 'dist');
const cache = path.join(temporary, 'cache');

try {
  await mkdir(docs, { recursive: true });
  await writeFile(
    path.join(source, 'content.config.ts'),
    [
      "import { defineCollection } from 'astro:content';",
      "import { docsLoader } from '@astrojs/starlight/loaders';",
      "import { docsSchema } from '@astrojs/starlight/schema';",
      '',
      'export const collections = {',
      "  docs: defineCollection({ loader: docsLoader(), schema: docsSchema() }),",
      '};',
      '',
    ].join('\n'),
    'utf8',
  );

  const perLanguage = Math.ceil(requested / 2);
  const writes = [];
  const directories = new Set();
  for (let index = 0; index < requested; index += 1) {
    const language = index < perLanguage ? 'en' : 'uk';
    const localIndex = language === 'en' ? index : index - perLanguage;
    const group = String(Math.floor(localIndex / 100)).padStart(2, '0');
    const page = String(localIndex + 1).padStart(4, '0');
    const directory = path.join(docs, language, 'scale', group);
    if (!directories.has(directory)) {
      await mkdir(directory, { recursive: true });
      directories.add(directory);
    }
    const body = `---\ntitle: "Synthetic page ${page}"\ndescription: "Disposable scale measurement page."\n---\n\n` +
      `This deterministic page measures the fixed cost of a normal Starlight content page. ` +
      `It contains prose, inline code such as \`value_${page}\`, and a small list.\n\n` +
      `## Explanation\n\nThe generated content is intentionally simple and is never published. ` +
      `The spike measures build time and output size at the requested page count.\n\n` +
      `- stable input\n- two locales\n- Pagefind indexing\n`;
    writes.push(writeFile(path.join(directory, `page-${page}.md`), body, 'utf8'));
    if (writes.length === 200) await Promise.all(writes.splice(0));
  }
  await Promise.all(writes);

  const started = performance.now();
  const code = await run(process.execPath, [astroCli, 'build', '--config', path.basename(config)], {
    cwd: siteRoot,
    env: {
      ...process.env,
      IQA_SCALE_SOURCE: source,
      IQA_SCALE_OUTPUT: output,
      IQA_SCALE_CACHE: cache,
    },
  });
  const seconds = (performance.now() - started) / 1000;
  if (code !== 0) throw new Error(`Astro scale build exited with ${code}`);

  const metrics = await treeMetrics(output);
  if (metrics.htmlPages !== requested) {
    throw new Error(`expected ${requested} HTML pages, built ${metrics.htmlPages}`);
  }
  console.log(
    JSON.stringify(
      {
        requested_pages: requested,
        built_html_pages: metrics.htmlPages,
        output_files: metrics.files,
        output_bytes: metrics.bytes,
        build_seconds: Number(seconds.toFixed(3)),
      },
      null,
      2,
    ),
  );
} finally {
  await rm(temporary, { recursive: true, force: true });
}

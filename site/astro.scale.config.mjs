import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

const source = process.env.IQA_SCALE_SOURCE;
const output = process.env.IQA_SCALE_OUTPUT;
const cache = process.env.IQA_SCALE_CACHE;

if (!source || !output || !cache) {
  throw new Error('scale spike paths were not supplied');
}

export default defineConfig({
  site: 'https://bogdan-kovalchuk.github.io',
  base: '/interview-qa',
  trailingSlash: 'always',
  srcDir: source,
  outDir: output,
  cacheDir: cache,
  integrations: [
    starlight({
      title: 'Interview QA scale spike',
      defaultLocale: 'en',
      locales: {
        en: { label: 'English', lang: 'en' },
        uk: { label: 'Українська', lang: 'uk' },
      },
      disable404Route: true,
      sidebar: [],
    }),
  ],
});

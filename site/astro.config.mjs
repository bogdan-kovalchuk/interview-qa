import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://bogdan-kovalchuk.github.io',
  base: '/interview-qa',
  trailingSlash: 'always',
  integrations: [
    starlight({
      title: 'Interview QA',
      defaultLocale: 'en',
      locales: {
        en: { label: 'English', lang: 'en' },
        uk: { label: 'Українська', lang: 'uk' },
      },
      disable404Route: true,
    }),
  ],
});

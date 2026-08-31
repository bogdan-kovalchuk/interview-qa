import { readFileSync } from 'node:fs';

import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

import { materialCodeThemes } from './src/styles/code-theme.mjs';

/**
 * The sidebar is generated, like the mirror it navigates: `tools/iqa/mirror.py`
 * writes it from `meta/taxonomy.md`'s order and `meta/vocabulary.yml`'s labels,
 * and `scripts/build.mjs` runs that before astro. Without an explicit sidebar
 * Starlight autogenerates one from the mirror's directory layout, which is
 * `{lang}/q/{id}/{slug}` - a menu of question ids, which is what this replaces.
 *
 * Missing file means the mirror has not run yet (a bare checkout, or `astro dev`
 * started by hand): fall back to no sidebar rather than failing to boot.
 */
function generatedSidebar() {
  try {
    return JSON.parse(readFileSync(new URL('./src/generated/sidebar.json', import.meta.url), 'utf8'));
  } catch {
    return [];
  }
}

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
      sidebar: generatedSidebar(),
      components: {
        // Renders inline code in a question title as `<code>` instead of
        // printing the backticks; see the component for why.
        PageTitle: './src/components/PageTitle.astro',
      },
      // Roboto and Roboto Mono are the reference site's fonts. They are taken
      // from npm rather than the Google Fonts stylesheet the reference links,
      // so the built site makes no third-party request; the faces are the same.
      customCss: [
        '@fontsource-variable/roboto/wght.css',
        '@fontsource-variable/roboto-mono/wght.css',
        './src/styles/material.css',
      ],
      expressiveCode: {
        themes: materialCodeThemes,
        // Expressive Code lightens a token colour until it clears 5.5:1 against
        // the code background. Material does no such thing, so leaving it on
        // silently shifts every dimmer token (punctuation, comments) away from
        // the reference. Off means the colours above are what actually renders.
        minSyntaxHighlightingColorContrast: 0,
        styleOverrides: {
          borderRadius: '0.1rem',
          borderWidth: '0',
          codePaddingBlock: '0.8rem',
          codePaddingInline: '1rem',
          frames: {
            shadowColor: 'transparent',
          },
        },
      },
    }),
  ],
});

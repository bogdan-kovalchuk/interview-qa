import { defineCollection, z } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

export const collections = {
  docs: defineCollection({
    loader: docsLoader(),
    schema: docsSchema({
      extend: z.object({
        slug: z.string().optional(),
        title_html: z.string().optional(),
        home_page: z.boolean().optional(),
        canonical: z.string().optional(),
        source_path: z.string().optional(),
        question_id: z.string().optional(),
        language: z.string().optional(),
        track: z.string().optional(),
        section: z.string().optional(),
        level: z.string().optional(),
        type: z.string().optional(),
        completeness: z.string().optional(),
      }),
    }),
  }),
};

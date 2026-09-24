import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const developers = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/developers' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    section: z.string().default('Guides'),
    order: z.number().default(100),
    status: z.enum(['ready', 'planned']).default('planned'),
  }),
});

export const collections = { developers };

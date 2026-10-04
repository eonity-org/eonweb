import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

// Lists every public page; developer pages come from the content collection.
export const GET: APIRoute = async ({ site }) => {
  const developers = await getCollection('developers');
  const paths = [
    '/',
    '/about/',
    ...developers.map((page) =>
      page.id === 'index' ? '/developers/' : `/developers/${page.id}/`,
    ),
  ];
  const urls = paths
    .map((path) => `  <url><loc>${new URL(path, site)}</loc></url>`)
    .join('\n');
  return new Response(
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls}\n</urlset>\n`,
    { headers: { 'Content-Type': 'application/xml; charset=utf-8' } },
  );
};

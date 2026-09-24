import { defineConfig } from 'astro/config';
import { satteri } from '@astrojs/markdown-satteri';
import externalLinks from './src/plugins/external-links.mjs';

export default defineConfig({
  site: 'https://eonity.org',
  output: 'static',
  markdown: {
    processor: satteri({
      hastPlugins: [externalLinks({ site: 'https://eonity.org' })],
    }),
  },
  trailingSlash: 'always',
  devToolbar: { enabled: false },
  vite: {
    server: {
      allowedHosts: ['web.eonweb.orb.local'],
    },
  },
});

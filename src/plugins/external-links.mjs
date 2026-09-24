// Apply the external-link policy to Markdown pages and content collections.
export default function externalLinks({ site }) {
  const origin = new URL(site).origin;
  return {
    name: 'external-links',
    element: {
      filter: ['a'],
      visit(node, ctx) {
        const properties = node.properties ?? {};
        if (typeof properties.href !== 'string') return;
        let url;
        try {
          url = new URL(properties.href, site);
        } catch {
          return;
        }
        if (
          !['http:', 'https:'].includes(url.protocol) ||
          url.origin === origin
        )
          return;
        const rel = Array.isArray(properties.rel)
          ? properties.rel
          : String(properties.rel ?? '')
              .split(/\s+/)
              .filter(Boolean);
        ctx.setProperty(node, 'target', '_blank');
        ctx.setProperty(node, 'rel', [
          ...new Set([...rel, 'noopener', 'noreferrer']),
        ]);
        ctx.setProperty(
          node,
          'title',
          properties.title
            ? `${properties.title} (opens in a new tab)`
            : 'Opens in a new tab',
        );
      },
    },
  };
}

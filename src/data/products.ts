// The Eonity products, in the order the site shows them. A new product is one
// entry here plus its page under src/pages/<id>/.
export interface Product {
  id: string;
  name: string;
  status: 'available' | 'coming';
  category: string;
  tagline: string;
  description: string;
  /** What the AI is given to work inside. */
  scope: string;
  /** What it can do there. */
  moves: string;
  href?: string;
  github?: string;
  logo?: { src: string; width: number; height: number };
}

export const products: Product[] = [
  {
    id: 'tydal',
    name: 'TYDAL',
    status: 'available',
    category: 'Digital assets',
    tagline: 'The typed Digital Asset Layer.',
    description:
      'Structure documents, images, datasets and code with schemas, enrich them with AI and share selected content through Vaults with people, applications and AI agents.',
    scope: 'A Vault',
    moves: 'Read, search and propose metadata',
    href: '/tydal/',
    github: 'https://github.com/eonity-org/tydal',
    logo: { src: '/brand/tydal.png?v=20261003-srgb', width: 315, height: 140 },
  },
  {
    id: 'tykerf',
    name: 'TYKERF',
    status: 'available',
    category: 'Web pages',
    tagline: 'Web pages, one block at a time.',
    description:
      'Cut a page into named blocks and change it through validated, undoable moves. Kaity, its AI, builds a page from a sentence and then works on the one block you select.',
    scope: 'A block of a page',
    moves: 'Split, move, resize and rewrite',
    href: '/tykerf/',
    github: 'https://github.com/eonity-org/tykerf',
    logo: { src: '/brand/tykerf-logo.svg', width: 294, height: 87 },
  },
  {
    id: 'tyset',
    name: 'TYSET',
    status: 'coming',
    category: 'Documents',
    tagline: 'Structured desktop publishing.',
    description:
      'The same approach for documents laid out page by page, in the tradition of structured authoring tools like FrameMaker. The AI works on one part of the document while you keep the final say.',
    scope: 'A part of a document',
    moves: 'Write, restructure and lay out',
  },
];

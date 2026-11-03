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
  /** What people and the AI do together with it, in one line. */
  together: string;
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
      'Structure documents, images, datasets and code with schemas. The AI proposes the descriptions; you approve them. Share selected content through Vaults with people, applications and AI agents.',
    scope: 'A Vault',
    moves: 'Read, search and propose metadata',
    together: 'Describe and share digital assets',
    href: '/tydal/',
    github: 'https://github.com/eonity-org/tydal',
    logo: { src: '/brand/tydal-logo.svg', width: 294, height: 118 },
  },
  {
    id: 'tykerf',
    name: 'TYKERF',
    status: 'available',
    category: 'Web pages',
    tagline: 'Web pages, one block at a time.',
    description:
      'Cut a page into named blocks. Point at anything, leave tasks, and hand them to Kaity, its AI, who changes only the block she is given. Every move can be undone.',
    scope: 'A block of a page',
    moves: 'Split, move, resize and rewrite',
    together: 'Build and improve web pages',
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
      'A structured document editor that opens Adobe FrameMaker MIF files. Publishers review, correct and translate their documents with an AI that works on one section at a time.',
    scope: 'A section of a document',
    moves: 'Review, correct and translate',
    together: 'Review, correct and translate publications',
    href: '/tyset/',
    logo: { src: '/brand/tyset-logo.svg', width: 224, height: 69 },
  },
];

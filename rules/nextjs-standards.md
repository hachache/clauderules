---
paths:
  - "**/app/**/*.{ts,tsx}"
  - "**/pages/**/*.{ts,tsx}"
---

# Standards Next.js 14+

## Server vs Client Components

```tsx
// Server Component (défaut) - pas de directive
async function UserList() {
  const users = await db.user.findMany();
  return <ul>{users.map(user => <li key={user.id}>{user.name}</li>)}</ul>;
}

// Client Component - interactivité
"use client";
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>Count: {count}</button>;
}
```

| Server Component | Client Component |
|-----------------|------------------|
| Fetch data | useState, useEffect |
| Accès backend | Event handlers |
| Tokens/secrets | Browser APIs |

## Data Fetching

```tsx
// Parallel data fetching
async function Dashboard() {
  const [user, posts] = await Promise.all([getUser(), getPosts()]);
  return <><UserProfile user={user} /><PostList posts={posts} /></>;
}

// Caching strategies
fetch(url, { cache: 'no-store' });           // Toujours fresh
fetch(url, { next: { revalidate: 60 } });    // ISR
```

## Server Actions

```tsx
"use server";
import { revalidatePath } from 'next/cache';

export async function createPost(formData: FormData) {
  const validated = CreatePostSchema.parse({
    title: formData.get('title'),
  });
  await db.post.create({ data: validated });
  revalidatePath('/posts');
}
```

## Metadata

```tsx
export async function generateMetadata({ params }): Promise<Metadata> {
  const product = await getProduct(params.id);
  return { title: product.name, description: product.description };
}
```

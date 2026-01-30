---
paths:
  - "**/*.jsx"
  - "**/*.tsx"
  - "**/components/**"
---

# Standards React / Next.js

## Architecture composants

### Structure projet Next.js

```
src/
├── app/                    # App Router (Next.js 13+)
├── components/
│   ├── ui/                 # Composants réutilisables
│   └── features/           # Composants métier
├── hooks/                  # Custom hooks (useXxx)
├── lib/                    # Utilities, API clients
├── contexts/               # React Contexts
└── types/                  # TypeScript types
```

## Composants fonctionnels

```tsx
interface UserCardProps {
  user: User;
  onSelect?: (user: User) => void;
  className?: string;
}

export function UserCard({ user, onSelect, className }: UserCardProps) {
  const handleClick = useCallback(() => {
    onSelect?.(user);
  }, [user, onSelect]);

  return (
    <div className={cn("rounded-lg p-4", className)} onClick={handleClick}>
      <h3>{user.name}</h3>
    </div>
  );
}
```

## Hooks patterns

```tsx
// React Query pour server state
function useUser(userId: string) {
  return useQuery({
    queryKey: ['user', userId],
    queryFn: () => api.getUser(userId),
    staleTime: 5 * 60 * 1000,
  });
}
```

## Performance

- `React.memo` pour composants purs
- `useMemo` pour calculs coûteux
- `useCallback` pour fonctions passées en props
- `lazy()` + `Suspense` pour code splitting

## Next.js

- Server Components par défaut
- `"use client"` uniquement si interactivité
- `fetch()` avec `next: { revalidate }` pour ISR

## Checklist

- [ ] Props typées avec interface
- [ ] Hooks extraits si > 10 lignes
- [ ] Keys stables sur les listes
- [ ] Cleanup dans useEffect
- [ ] Error boundaries
- [ ] Loading states

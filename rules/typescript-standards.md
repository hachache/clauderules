---
paths:
  - "**/*.ts"
  - "**/*.tsx"
---

# Standards TypeScript

## Principes

- **Strict mode** : `strict: true` dans tsconfig
- **No any** : utiliser `unknown` si type inconnu
- **Explicit** : typer les retours de fonctions publiques

## Types vs Interfaces

```typescript
// Interface - pour objets, extensible
interface User {
  id: string;
  name: string;
}

// Type - pour unions, tuples
type Status = 'pending' | 'active' | 'inactive';
type Coordinate = [number, number];
```

## Narrowing & Guards

```typescript
function isUser(value: unknown): value is User {
  return typeof value === 'object' && value !== null && 'id' in value;
}

// Discriminated unions
type Result<T> =
  | { success: true; data: T }
  | { success: false; error: string };
```

## Generics

```typescript
function first<T>(array: T[]): T | undefined {
  return array[0];
}

interface Repository<T> {
  findById(id: string): Promise<T | null>;
  create(data: Omit<T, 'id'>): Promise<T>;
}
```

## Utility Types

```typescript
type UpdateUser = Partial<User>;           // Tous optionnels
type UserPreview = Pick<User, 'id' | 'name'>;  // Sélection
type CreateUser = Omit<User, 'id'>;        // Exclusion
type ApiResponse = Awaited<ReturnType<typeof fetchUser>>;
```

## Patterns

```typescript
// as const pour littéraux
const ROLES = ['admin', 'user'] as const;
type Role = typeof ROLES[number];

// satisfies pour validation
const config = {
  port: 3000,
} satisfies ServerConfig;
```

## Checklist

- [ ] `strict: true`
- [ ] Pas de `any`
- [ ] Types de retour explicites
- [ ] Generics pour code réutilisable
- [ ] Discriminated unions pour états

---
paths:
  - "**/*.jsx"
  - "**/*.tsx"
  - "**/*.vue"
---

# Standards Tailwind CSS

## Principes

- **Utility-first** : composer avec des classes utilitaires
- **Mobile-first** : breakpoints s'appliquent vers le haut
- **Design tokens** : utiliser les valeurs du thème

## Organisation classes

```tsx
// Ordre: Layout → Spacing → Sizing → Typography → Visual → Interactive
<div className="
  flex items-center justify-between
  p-4 mx-auto
  w-full max-w-md
  text-sm font-medium text-gray-900
  bg-white rounded-lg shadow-md
  hover:shadow-lg transition-shadow
">
```

## Utility cn() pour conditionnels

```tsx
import { clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

<button className={cn(
  "px-4 py-2 rounded-lg font-medium",
  variant === "primary" && "bg-blue-600 text-white",
  disabled && "opacity-50 cursor-not-allowed"
)}>
```

## Responsive

```tsx
<div className="
  flex flex-col        // Mobile: colonne
  md:flex-row          // Tablet+: ligne
  lg:items-center      // Desktop+: centré
">
```

## Dark mode

```tsx
<div className="
  bg-white text-gray-900
  dark:bg-gray-900 dark:text-gray-100
">
```

## Éviter

- Valeurs arbitraires `w-[347px]` sauf exception
- `!important`
- Styles inline avec Tailwind

## Checklist

- [ ] Mobile-first
- [ ] Composants extraits si pattern répété 3+ fois
- [ ] cn() pour classes conditionnelles
- [ ] Dark mode supporté si requis
- [ ] Focus states pour accessibilité

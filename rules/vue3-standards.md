---
paths:
  - "**/*.vue"
---

# Standards Vue 3 Composition API

## Structure composant

```vue
<script setup lang="ts">
// 1. Imports
// 2. Props & Emits
// 3. Composables & Stores
// 4. Reactive state
// 5. Computed
// 6. Watchers
// 7. Lifecycle
// 8. Methods
</script>
```

## Structure projet

```
src/
├── components/
│   ├── ui/              # Composants UI génériques
│   └── features/        # Composants métier
├── composables/         # Logique réutilisable (useXxx)
├── stores/              # Pinia stores
├── views/               # Pages
└── types/               # TypeScript types
```

## Composables

```typescript
export function useUser(userId: Ref<string> | string) {
  const user = ref<User | null>(null)
  const isLoading = ref(true)

  async function fetchUser() {
    isLoading.value = true
    user.value = await api.getUser(unref(userId))
    isLoading.value = false
  }

  watch(() => unref(userId), fetchUser, { immediate: true })

  return { user, isLoading, refetch: fetchUser }
}
```

## Pinia Store

```typescript
export const useUserStore = defineStore('user', () => {
  const currentUser = ref<User | null>(null)

  const isAdmin = computed(() => currentUser.value?.role === 'admin')

  async function login(email: string, password: string) {
    const response = await api.login({ email, password })
    currentUser.value = response.user
  }

  return { currentUser, isAdmin, login }
})
```

## Props & Emits typés

```typescript
const props = withDefaults(defineProps<{
  title: string
  variant?: 'primary' | 'secondary'
}>(), {
  variant: 'primary',
})

const emit = defineEmits<{
  select: [user: User]
  close: []
}>()
```

## Checklist

- [ ] `<script setup lang="ts">`
- [ ] Props et emits typés
- [ ] Composables pour logique réutilisable
- [ ] Pinia pour state global
- [ ] `computed()` pour valeurs dérivées
- [ ] Keys uniques sur v-for

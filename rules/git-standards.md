---
paths:
  - "**/*"
---

# Git Standards

## Conventional Commits

```
<type>(<scope>): <description>

[body optionnel]
[footer optionnel]
```

| Type | Usage |
|------|-------|
| `feat` | Nouvelle fonctionnalité |
| `fix` | Correction de bug |
| `docs` | Documentation |
| `refactor` | Refactoring |
| `test` | Tests |
| `chore` | Maintenance |

```bash
# ✅ BON
feat(auth): add JWT token refresh mechanism
fix(api): handle null response from external service

# ❌ MAUVAIS
updated stuff
fix bug
```

## GitFlow Workflow

| Branche | Description |
|---------|-------------|
| `main` | Production, jamais de commit direct |
| `develop` | Intégration |

```
feature/123-user-auth    → develop
release/v1.2.0           → main + develop
hotfix/v1.2.1            → main + develop
```

## Commandes GitFlow

```bash
# Feature
git checkout develop && git checkout -b feature/123-description
git checkout develop && git merge --no-ff feature/123-description

# Release
git checkout -b release/v1.2.0
git checkout main && git merge --no-ff release/v1.2.0
git tag -a v1.2.0 -m "Release v1.2.0"
git checkout develop && git merge --no-ff release/v1.2.0
```

## Semantic Versioning

```
MAJOR.MINOR.PATCH

MAJOR → Breaking changes
MINOR → Nouvelles features (rétrocompatible)
PATCH → Bug fixes
```

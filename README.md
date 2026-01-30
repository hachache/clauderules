# 🧠 Claude Code Rules

Collection de règles pour [Claude Code](https://claude.ai/code) - l'assistant IA d'Anthropic en ligne de commande.

Ces règles permettent à Claude de suivre automatiquement vos standards de développement, conventions de code, et bonnes pratiques.

## 📁 Structure

```
.claude/
├── CLAUDE.md              # Instructions globales (toujours chargé)
├── settings.json          # Configuration des hooks
├── rules/                 # Règles conditionnelles
│   ├── typescript-standards.md
│   ├── python-standards.md
│   ├── react-standards.md
│   ├── nextjs-standards.md
│   ├── fastapi-standards.md
│   ├── testing-standards.md
│   ├── database-standards.md
│   ├── git-standards.md
│   └── ...
├── hooks/                 # Scripts de validation
│   └── conventional-commits.py
└── agents/                # Agents spécialisés
    ├── devops-expert.md
    └── security-auditor.md
```

## 🚀 Installation

### Option 1 : Clone complet (recommandé)

```bash
# Dans votre dossier home ou projet
git clone git@github.com:hachache/clauderules.git .claude
```

### Option 2 : Copie sélective

```bash
# Cloner le repo
git clone git@github.com:hachache/clauderules.git

# Copier les règles souhaitées
cp -r clauderules/rules ~/.claude/rules
cp clauderules/CLAUDE.md ~/.claude/
```

## 📖 Comment ça marche

### Hiérarchie de chargement

Claude Code charge les règles dans cet ordre (du plus global au plus spécifique) :

```
~/.claude/CLAUDE.md                    # Global (tous projets)
~/.claude/rules/*.md                   # Règles globales conditionnelles
/chemin/projet/.claude/CLAUDE.md       # Projet spécifique
/chemin/projet/.claude/rules/*.md      # Règles projet conditionnelles
```

### Règles conditionnelles (paths)

Les règles dans `rules/` utilisent un frontmatter `paths:` pour s'activer uniquement sur certains fichiers :

```markdown
---
paths:
  - "**/*.ts"
  - "**/*.tsx"
---

# Standards TypeScript

- Strict mode obligatoire
- Pas de `any`, utiliser `unknown`
- Types de retour explicites
```

**Exemple concret** : Quand vous travaillez sur `app/components/Button.tsx`, Claude charge automatiquement :
- `CLAUDE.md` (toujours)
- `typescript-standards.md` (match `**/*.tsx`)
- `react-standards.md` (si configuré pour `**/*.tsx`)

### CLAUDE.md global

Le fichier `CLAUDE.md` est **toujours** chargé. Idéal pour :

```markdown
# Instructions Globales

## Style de code
- Français dans les commentaires
- Anglais pour le code
- Conventional Commits obligatoire

## Préférences
- Préférer composition à héritage
- Tests obligatoires pour toute nouvelle feature
- Documentation JSDoc pour les fonctions publiques
```

## 🎯 Règles incluses

| Fichier | Activation | Description |
|---------|------------|-------------|
| `typescript-standards.md` | `**/*.ts, **/*.tsx` | TypeScript strict, generics, utility types |
| `python-standards.md` | `**/*.py` | Pydantic, async, type hints |
| `react-standards.md` | `**/*.tsx, **/*.jsx` | Hooks, React Query, Server Components |
| `nextjs-standards.md` | `**/app/**/*.tsx` | App Router, Server Actions, ISR |
| `fastapi-standards.md` | `**/api/**/*.py` | Schemas, DI, async endpoints |
| `testing-standards.md` | `**/*.test.*, **/*.spec.*` | Jest, Playwright, pytest |
| `database-standards.md` | `**/*.prisma, **/models/**` | Prisma, SQLAlchemy, migrations |
| `git-standards.md` | `**/*` | Conventional Commits, GitFlow |

## 🔧 Hooks (validation automatique)

Les hooks permettent de valider les actions de Claude **avant** qu'elles ne soient exécutées.

### Configuration (`settings.json`)

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/conventional-commits.py"
          }
        ]
      }
    ]
  }
}
```

### Exemple : Validation des commits

```python
#!/usr/bin/env python3
# hooks/conventional-commits.py

import sys
import json
import re

PATTERN = r'^(feat|fix|docs|style|refactor|perf|test|chore)(\(.+\))?!?: .+'

input_data = json.loads(sys.stdin.read())
command = input_data.get("tool_input", {}).get("command", "")

if "git commit" in command:
    # Extraire le message
    match = re.search(r'-m ["\'](.+?)["\']', command)
    if match:
        message = match.group(1)
        if not re.match(PATTERN, message):
            print(json.dumps({
                "decision": "block",
                "reason": "❌ Format: type(scope): description"
            }))
            sys.exit(0)

print(json.dumps({"decision": "approve"}))
```

## 🤖 Agents spécialisés

Les agents sont des prompts réutilisables pour des tâches spécifiques :

```markdown
<!-- agents/security-auditor.md -->
# Security Auditor

Tu es un expert en sécurité applicative.

## Checklist OWASP Top 10
- [ ] Injection (SQL, NoSQL, OS)
- [ ] Broken Authentication
- [ ] Sensitive Data Exposure
...
```

Utilisation dans Claude Code :
```
> @security-auditor audite ce endpoint d'authentification
```

## 💡 Personnalisation

### Ajouter une nouvelle règle

1. Créer le fichier dans `rules/` :

```markdown
---
paths:
  - "**/kubernetes/**/*.yaml"
  - "**/k8s/**/*.yaml"
---

# Standards Kubernetes

## Ressources
- Toujours définir requests ET limits
- Labels obligatoires : app, env, version
- Utiliser des namespaces dédiés
```

2. La règle s'active automatiquement sur les fichiers matchant les paths.

### Désactiver une règle

Supprimer ou renommer le fichier (ex: `typescript-standards.md.disabled`).

## 🔗 Liens utiles

- [Documentation Claude Code](https://docs.anthropic.com/claude-code)
- [Memory & Rules](https://docs.anthropic.com/claude-code/memory)
- [Hooks System](https://docs.anthropic.com/claude-code/hooks)

## 📝 License

MIT - Utilisez et adaptez librement ces règles pour vos projets.

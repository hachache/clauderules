# Standards de Code Globaux

## Nommage
- Noms explicites, pas d'abréviations (sauf standards : ip, tls, uid)
- Variables et fonctions qui expriment l'intention sans ambiguïté

## Structure
- Fonctions courtes, pures, une seule responsabilité
- Pas de commentaires inutiles - si nécessaire, renommer ou refactorer
- Code lisible de haut en bas, zéro friction cognitive

## Gestion des erreurs
- Erreurs explicites et contextuelles, jamais silencieuses
- Toujours propager le contexte d'erreur

## Architecture
- Séparation des responsabilités stricte
- Pas de logique métier dans les vues/handlers
- Effets de bord aux frontières, logique pure au centre
- Injection de dépendances, pas d'état global

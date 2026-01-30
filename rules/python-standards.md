---
paths:
  - "**/*.py"
---

# Standards Python

## Typage obligatoire

```python
# ❌ MAUVAIS
def process_data(data):
    return data.get("value")

# ✅ BON
def process_data(data: dict[str, Any]) -> str | None:
    """Extract value from data dictionary."""
    return data.get("value")
```

## Structure des fichiers

```
src/
  models/         # Pydantic models
  services/       # Business logic
  controllers/    # Routes/handlers
  utils/          # Helpers
tests/
  test_*.py       # Tests pytest
```

## Gestion des erreurs

```python
# ✅ Contexte explicite
try:
    result = fetch_remote_data(endpoint)
except RequestError as error:
    logger.error("Failed to fetch data", extra={
        "endpoint": endpoint,
        "error": str(error)
    })
    raise DataFetchError(f"Unable to retrieve {endpoint}") from error
```

## Tests avec pytest

```python
def test_process_data_returns_value() -> None:
    """Should extract value from valid data."""
    data = {"value": "expected"}
    result = process_data(data)
    assert result == "expected"
```

## Style

- Snake_case pour variables et fonctions
- PascalCase pour classes
- SCREAMING_SNAKE_CASE pour constantes
- Docstrings PEP 257 pour toutes les fonctions publiques
- Ruff pour le formatage

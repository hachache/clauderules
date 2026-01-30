---
paths:
  - "**/*.test.{ts,tsx,js}"
  - "**/*.spec.{ts,tsx,js}"
  - "**/tests/**/*.py"
  - "**/__tests__/**/*"
---

# Standards de Tests

## Principes généraux

- **AAA Pattern** : Arrange, Act, Assert
- **Un test = un comportement** : pas de tests qui testent plusieurs choses
- **Noms descriptifs** : should_return_user_when_valid_id
- **Indépendance** : les tests ne dépendent pas les uns des autres
- **Déterministes** : même résultat à chaque exécution

## Jest / Vitest (JavaScript/TypeScript)

```typescript
// Mock dependencies BEFORE imports
jest.mock('../api/userService', () => ({
  fetchUser: jest.fn(),
}));

import { fetchUser } from '../api/userService';

describe('getUserData', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('should return user data when fetch is successful', async () => {
    // Arrange
    const mockUser = { id: 1, name: 'John' };
    (fetchUser as jest.Mock).mockResolvedValue(mockUser);

    // Act
    const result = await getUserData(1);

    // Assert
    expect(result).toEqual(mockUser);
    expect(fetchUser).toHaveBeenCalledWith(1);
  });
});
```

## Playwright (E2E)

```typescript
test.describe('Login Page', () => {
  test('should login with valid credentials', async ({ page }) => {
    await page.getByTestId('email').fill('valid@test.com');
    await page.getByTestId('password').fill('password123');
    await page.getByTestId('submit').click();

    await expect(page.getByTestId('dashboard')).toBeVisible();
  });
});

// Sélecteurs priorité
page.getByRole('button', { name: 'Submit' })  // 1. Rôle accessible
page.getByTestId('submit-button')              // 2. Test ID
page.getByText('Submit')                       // 3. Texte visible
```

## pytest (Python)

```python
class TestUserService:
    @pytest.fixture
    def user_service(self):
        return UserService(repository=Mock())

    def test_get_user_returns_user_when_found(self, user_service, mock_user):
        # Arrange
        user_service.repository.find_by_id.return_value = mock_user

        # Act
        result = user_service.get("1")

        # Assert
        assert result == mock_user

@pytest.mark.parametrize("input,expected", [
    ("", False),
    ("valid@email.com", True),
])
def test_is_valid_email(input, expected):
    assert is_valid_email(input) == expected
```

## Couverture

| Type | Quoi tester | Proportion |
|------|-------------|------------|
| Unit | Fonctions pures, utils | 70% |
| Integration | API, DB queries | 20% |
| E2E | Parcours critiques | 10% |

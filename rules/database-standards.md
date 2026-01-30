---
paths:
  - "**/*.prisma"
  - "**/migrations/**"
  - "**/models/**/*.py"
  - "**/db/**/*"
---

# Standards Bases de Données

## Principes

- **Normalisation** : 3NF minimum
- **Indexes** : colonnes WHERE, JOIN, ORDER BY
- **Contraintes** : NOT NULL, UNIQUE, FK au niveau DB
- **Nommage** : snake_case, tables pluriel

## Prisma (TypeScript)

```prisma
model User {
  id        String   @id @default(cuid())
  email     String   @unique
  name      String
  posts     Post[]
  createdAt DateTime @default(now()) @map("created_at")

  @@map("users")
  @@index([email])
}
```

```typescript
// Select uniquement nécessaire
const users = await prisma.user.findMany({
  select: { id: true, name: true },
});

// Include évite N+1
const usersWithPosts = await prisma.user.findMany({
  include: { posts: { where: { published: true } } },
});

// Transactions
const [user, post] = await prisma.$transaction([
  prisma.user.create({ data: userData }),
  prisma.post.create({ data: postData }),
]);
```

## SQLAlchemy (Python)

```python
class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False, index=True)
    posts = relationship("Post", back_populates="author")

# Eager loading
users = session.query(User).options(joinedload(User.posts)).all()
```

## Migrations

```bash
# Prisma
npx prisma migrate dev --name add_user_role
npx prisma migrate deploy

# Alembic
alembic revision --autogenerate -m "add user role"
alembic upgrade head
```

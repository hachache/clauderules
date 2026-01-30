---
paths:
  - "**/server/**/*.ts"
  - "**/api/**/*.ts"
  - "**/backend/**/*.ts"
---

# Standards Node.js / Express

## Structure projet

```
server/
├── src/
│   ├── app.ts              # Configuration Express
│   ├── routes/             # Route handlers
│   ├── controllers/        # Business logic
│   ├── services/           # Domain services
│   ├── models/             # Database models
│   ├── middleware/         # Custom middleware
│   └── utils/              # Helpers
└── tests/
```

## Configuration Express

```typescript
import express from 'express';
import helmet from 'helmet';
import cors from 'cors';
import rateLimit from 'express-rate-limit';

const app = express();

// Security
app.use(helmet());
app.use(cors({ origin: process.env.FRONTEND_URL, credentials: true }));
app.use('/api/', rateLimit({ windowMs: 15 * 60 * 1000, max: 100 }));

// Parsing
app.use(express.json({ limit: '10mb' }));

// Routes
app.use('/api/auth', authRouter);

// Error handling (toujours en dernier)
app.use(errorHandler);
```

## Error handler centralisé

```typescript
export class AppError extends Error {
  constructor(
    public statusCode: number,
    public message: string,
    public code?: string
  ) {
    super(message);
  }
}

export function errorHandler(err: Error, req: Request, res: Response, next: NextFunction) {
  if (err instanceof AppError) {
    return res.status(err.statusCode).json({
      error: { code: err.code, message: err.message }
    });
  }

  // Ne pas exposer les erreurs internes
  res.status(500).json({
    error: { code: 'INTERNAL_ERROR', message: 'An unexpected error occurred' }
  });
}
```

## Validation avec Zod

```typescript
import { z } from 'zod';

const createUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(2).max(100),
  password: z.string().min(8),
});

router.post('/users', validate(createUserSchema), createUser);
```

## Checklist

- [ ] Helmet pour headers sécurité
- [ ] CORS configuré explicitement
- [ ] Rate limiting
- [ ] Validation inputs (Zod)
- [ ] Error handler centralisé
- [ ] Pas d'erreurs internes exposées
- [ ] Logging structuré

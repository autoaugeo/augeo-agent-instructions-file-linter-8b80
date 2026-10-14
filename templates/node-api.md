# CLAUDE.md: Node.js API

Fill in each <FILL IN>, delete the hint in parentheses, and remove any section that does not apply. Aim to stay under 200 lines.

## Project overview

- Name: <FILL IN: service name>
- Purpose: <FILL IN: one sentence on what the API serves and who calls it>
- Runtime: <FILL IN: e.g. Node 20 LTS>
- Framework: <FILL IN: e.g. Express, Fastify, Hono or NestJS>
- Language: <FILL IN: TypeScript or JavaScript>
- Database: <FILL IN: e.g. PostgreSQL via Prisma, or none>
- Entry point: <FILL IN: e.g. src/server.ts>

## Commands

- Install: `<FILL IN: e.g. npm ci>`
- Dev server: `<FILL IN: e.g. npm run dev>`
- Build: `<FILL IN: e.g. npm run build>`
- Run all tests: `<FILL IN: e.g. npm test>`
- Run one test file: `<FILL IN: e.g. npx vitest run test/users.test.ts>`
- Lint: `<FILL IN: e.g. npm run lint>`
- Type check: `<FILL IN: e.g. npx tsc --noEmit>`
- Database migrations: `<FILL IN: e.g. npx prisma migrate dev>`

## Code style

- Formatter: <FILL IN: e.g. Prettier with the repo config>; run it instead of formatting by hand.
- Use `async`/`await`, not raw promise chains.
- Naming: `camelCase` for variables and functions, `PascalCase` for types and classes.
- Request bodies and query strings are validated at the edge with <FILL IN: e.g. zod>.
- Module system: <FILL IN: ES modules or CommonJS>.
- Errors: throw <FILL IN: your error class> and let the error middleware format the response.

## Directory map

- `src/routes/`: route definitions, one file per resource.
- `src/services/`: business logic, no HTTP types.
- `src/db/`: queries, models and migrations.
- `src/middleware/`: auth, logging, error handling.
- `test/`: tests mirroring `src/`.
- <FILL IN: any other directory, e.g. `openapi/`>

## Do

- Keep route handlers thin; put logic in services.
- Return consistent error JSON: <FILL IN: shape, e.g. { "error": { "code", "message" } }>.
- Read configuration from environment variables through <FILL IN: config module>.
- Add or update an API test with every endpoint change.
- Document new endpoints in <FILL IN: e.g. openapi.yaml, or README>.

## Don't

- Don't commit secrets or `.env` files; use `.env.example` for names only.
- Don't log request bodies that may hold personal data or credentials.
- Don't build SQL by string concatenation.
- Don't add a dependency without asking first.
- Don't change existing response shapes without noting a breaking change.

## Testing

- Framework: <FILL IN: e.g. Vitest, Jest or node:test>.
- Test files: <FILL IN: e.g. `*.test.ts` under `test/`>.
- Integration tests use: <FILL IN: e.g. supertest against an in-memory app, a test database>.
- External services in tests: <FILL IN: e.g. mocked, never called>.
- Before saying a task is done, run: `<FILL IN: e.g. npm run lint && npx tsc --noEmit && npm test>`

## Commit and PR conventions

- Commit message format: <FILL IN: e.g. "feat: add GET /users/:id">.
- One logical change per commit; keep migrations in the same PR as the code that needs them.
- Branch names: <FILL IN: e.g. feature/short-name>.
- PR checklist: <FILL IN: e.g. tests pass, docs updated>.

## Known gotchas

- <FILL IN: e.g. "tests need a local database on port 5433">
- <FILL IN: a second gotcha, or delete this line>

---
AI-generated. Checked only by an automated script. Independent product, not affiliated with or endorsed by Anthropic.

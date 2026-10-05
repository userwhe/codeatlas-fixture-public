# CodeAtlas public fixture

A small Python and TypeScript repository for CodeAtlas indexing and citation checks.
All content is synthetic sample code and contains no real credentials or private business data.

## Files

- `backend/permissions.py`: repository allowlist and external-processing consent checks.
- `backend/service.py`: a connection service that calls those checks.
- `frontend/types.ts`: typed request and response shapes.
- `frontend/client.ts`: a minimal API client.
- `docs/architecture.md`: architecture and supported behavior.

## Questions to try

1. Where are repository permissions checked?
2. When is external-processing consent required?
3. Which TypeScript function connects a repository?
4. Which payment provider does this use? (Expected: insufficient evidence.)

## CodeAtlas connection check

Install your development GitHub App on this repository before connecting it.
For the private fixture, connecting without external-processing acceptance should return
`external_processing_not_accepted`; accepting should allow indexing.
Verify this behavior in CodeAtlas: storing the fixture on GitHub does not enforce the gate.

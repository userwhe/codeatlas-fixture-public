# Architecture

The Python demo service checks repository access before checking external-processing consent.
The TypeScript client submits a repository ID and a consent flag to CodeAtlas.
These files are indexing fixtures, not a running web application: the Python service and
TypeScript client are independent examples and are not wired together.

## Supported behavior

- Access is restricted to an explicit user allowlist.
- Private repositories require external-processing acceptance.
- The fixture does not execute imported repositories.
- There is no payment integration.

## Re-indexing check

After a new commit, manually re-index this repository in CodeAtlas.
The new snapshot should include this section, while earlier answers should
keep their original commit-specific citations.

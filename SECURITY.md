# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| 0.4.x   | yes       |
| 0.3.x   | no        |

## Reporting a vulnerability

This is a game-modding tool that reads/writes process memory of a running DOTA2 client.
That's the whole point of the project — please don't file issues about that.

What we *do* care about:

- Memory corruption / arbitrary code execution in our own process (the injector
  parsing untrusted signature files, the C# native helper misreading a handle, etc.)
- Privilege escalation from the loader when the game runs as a different user.
- Bundled Python wheels that don't match the hashes in `requirements.txt`.

Email `security@dota2-modmenu.dev` with a proof-of-concept. We'll respond within 72h.
Responsible disclosure appreciated; public shaming less so.

## Out of scope

- VAC bans incurred by using this tool. Use at your own risk, ideally on a burner.
- Anti-cheat detection. Working around VAC is not a project goal — this is an offline
  / custom-lobby / bot-match tool by design.
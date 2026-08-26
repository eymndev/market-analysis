# BISTECH VERDA HTTP REST v1.10 summary

This summary is based on the integration manual dated October 14, 2022. Current Borsa Istanbul documentation and institutional permissions control live access.

## Access and authentication

- Production internet base URL: `https://verda.borsaistanbul.com/`
- Access requires a Borsa Istanbul API application user and permissions for specific file types.
- Every request uses HTTP Basic Authentication.
- Never place credentials in source files, URLs, command arguments, or logs. The root client reads `BIST_VERDA_USER` and `BIST_VERDA_PASSWORD` from the environment.

## Read-only endpoints

- `GET /files` lists only the file types authorized for the current user. Important fields include `id`, name, `frequency`, `expectedGenerationTime`, `json`, `lastGenerated`, `lastGeneratedFilename`, and `links`.
- `GET /files/download` requires `type`; optional parameters include `year`, `month`, `day`, `hour`, `session`, and `media=json`.
- Responses may be JSON or files. Some file types are ZIP archives.

## Errors and diagnostics

- `401`: invalid credentials or a blocked/inactive user.
- `403`: invalid user type, missing file permission, or a file that cannot be downloaded through the API.
- `404`: no file matches the date, hour, or session criteria.
- `415`: the file type is not available as JSON; retry without `media=json`.
- `500`: BIST-side failure. Record the `X-Request-Id`, but never log credentials or licensed file contents.

`POST /change-password` is outside this analysis plugin's normal scope. Do not call it unless the user explicitly requests that operation.

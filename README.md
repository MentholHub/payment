# payment

## Create virtual environment

```bash
uv venv
source .venv/bin/activate # Linux (bash)
uv sync
```

## Format code

```bash
nox --session format
# OR
uvx nox -s format
```

## Lint code

```bash
nox --session lint
# OR
uvx nox -s lint
```

## Test code

```bash
nox --session test
# OR
uvx nox -s test
```

lint:
	uvx nox -s lint

format:
	uvx nox -s format

test:
	uvx nox -s test

check:
	uv run pre-commit run --show-diff-on-failure --color=always --all-files

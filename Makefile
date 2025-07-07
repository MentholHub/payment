lint:
	uvx nox -s lint

format:
	uvx nox -s format

test:
	uvx nox -s test

check:
	uvx pre-commit run -a

typecheck:
	uvx nox -s typecheck

stress:
	uvx nox -s stress

mutants:
	uvx nox -s mutants

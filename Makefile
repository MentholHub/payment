lint:
	uvx nox -s lint

format:
	uvx nox -s format

test:
	uvx nox -s test

check:
	uvx pre-commit run -a

typecheck:
	uvx pyrefly check src/payment 

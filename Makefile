lock:
	@echo "Run locking..."
	@uv lock
	@echo "Done"

update:
	@echo "Run updating..."
	@uv lock --upgrade
	@echo "Done"

format:
	@echo "Run formatting..."
	@find src/ tests/ -type f -name "*.py" -print0 | xargs -0 uvx autopep8 -i -a -a
	@echo "Done"
	@echo "Run imports sorting..."
	@uvx isort src/ tests/
	@echo "Done"

lint:
	@echo "Run flake8 linting..."
	@uvx flake8 src/ tests/
	@echo "Done"
	@echo "Run ty checking..."
	@uvx ty check src/
	@echo "Done"

run:
	@echo "Run app..."
	@docker compose down -v
	@docker compose up -d --build

test:
	@echo "Run testing..."
	@pytest -v -s --tb=short --strict-markers -n=auto tests/
	@echo "Done"

migrate:
	@echo "Apply migrations..."
	@docker compose exec web alembic upgrade head
	@echo "Done"

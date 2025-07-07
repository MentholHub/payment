# payment

<div align="center">
<p>Статус прохождения тестов и линтера</p>
<img src="https://github.com/MentholHub/payment/actions/workflows/test.yml/badge.svg">
<img src="https://github.com/MentholHub/payment/actions/workflows/linter.yml/badge.svg">
</div>

---

**Не забывайте про pre-commit**:

```bash
pre-commit run -a
```

## Зависимости

### Основные

 + adaptix>=3.0.0b11 - валидация моделей
 + aiocache>=0.12.3 - асинхронное кэширование
 + dishka>=1.6.0 - depedency injection, внедрение зависимостей
 + faststream>=0.5.44 - управление брокерами сообщений
 + orjson>=3.10.18 - быстрая сериализация и десериализация json
 + pre-commit>=4.2.0 - pre-commit
 + redis>=6.2.0 - редис
 + sqlalchemy>=2.0.41 - ORM

### Dev

 + pyrefly>=0.22.2 - статический анализатор типов
 + black>=25.1.0 - форматирование
 + isort>=6.0.1 - сортировка импортов
 + nox>=2025.5.1 - автоматизация сессий
 + pytest>=8.4.1 - тестирование
 + pytest-coverage>=0.0 - проверка покрытия кода тестами
 + ruff>=0.12.2 - линтер-форматтер
 + locust>=2.37.11 - стресс-тесты
 + mutmut>=3.3.0 - тестирование с мутациями

---

## Создайте виртуальное окружение через uv

```bash
uv venv
source .venv/bin/activate # Linux (bash)
uv sync
```

## Форматирование кода

```bash
nox --session format
# ИЛИ
uvx nox -s format
```

## Линтинг кода

```bash
nox --session lint
# ИЛИ
uvx nox -s lint
```

## Тестирование кода

```bash
nox --session test
# ИЛИ
uvx nox -s test
```

## Проверка типов

```bash
nox --session typecheck
# ИЛИ
uvx nox -s typecheck
```

## Стресс-тест

```bash
nox --session stress
# ИЛИ
uvx nox -s stress
```

## Тестирование с мутантами

```bash
nox --session mutants
# ИЛИ
uvx nox -s mutants
```

## Makefile

```bash
make format # format
make lint # lint
make test # test
make check # pre-commit
make typecheck # type check
make stress # stress test
make mutants
```

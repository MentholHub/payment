# Payment service

#### CI/CD status
<img src="https://github.com/MentholHub/payment/actions/workflows/ci.yml/badge.svg">

## Взаимодействие
```shell
$ git clone git@github.com:MentholHub/payment.git
$ cd payment
$ make install

$ source .venv/bin/activate
$ uv sync
$ # Теперь все готово к работе

$ make install # Синхронизирует зависимости и создет виртуальную среду
$ make lock # Создает lock-файл
$ make update # Обновляет все зависимости
$ make format # Форматирует все файлы
$ make lint # Запускает линтеры
$ make test # Запускает тесты
$ make run # Запускает приложение на порте :8000

$ uvx pre-commit run -a # Не забывайте делать пре-коммит
```

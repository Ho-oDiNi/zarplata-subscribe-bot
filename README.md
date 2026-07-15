# Zarplata Subscribe Bot

Telegram-бот с FastAPI-эндпоинтом для обработки webhook-уведомлений Ghost.
Для релиза бота обязательно использовать SSL-сертификат: Ghost отправляет webhooks только по HTTPS.

## Переменные окружения

Создайте файл `config/.env` по примеру:

```bash
cp config/.env.example config/.env
```

Доступные настройки:

| Переменная | Описание | Значение по умолчанию |
| --- | --- | --- |
| `API_TOKEN` | Токен Telegram-бота | обязательная |
| `ADMIN` | Telegram ID администратора | обязательная |
| `BOT_HOST` | Хост FastAPI внутри контейнера | `0.0.0.0` |
| `BOT_PORT` | Порт FastAPI внутри контейнера | `8000` |
| `DATABASE_PATH` | Путь к SQLite базе | `utils/database.db` |
| `APP_PORT` | Порт на хосте для Docker Compose | `8000` |

## Запуск в Docker

```bash
docker compose up -d --build
```

Контейнер публикует FastAPI на порту `8000` и хранит SQLite-базу в каталоге `./data` через volume.
Проверка работоспособности:

```bash
curl http://localhost:8000/
```

## Автоматический деплой через GitHub Actions

Workflow `.github/workflows/deploy.yml` запускается при push в `main` и вручную через `workflow_dispatch`.
Он собирает Docker-образ для проверки, подключается к серверу по SSH, обновляет код и выполняет:

```bash
docker compose up -d --build --remove-orphans
```

Добавьте в GitHub Secrets репозитория:

| Secret | Описание |
| --- | --- |
| `SERVER_HOST` | IP или домен сервера |
| `SERVER_USER` | SSH-пользователь на сервере |
| `SERVER_SSH_KEY` | Приватный SSH-ключ для доступа к серверу |
| `SERVER_PORT` | SSH-порт, можно не задавать при стандартном `22` |
| `SERVER_APP_DIR` | Путь к каталогу приложения на сервере |
| `API_TOKEN` | Токен Telegram-бота для первичного создания `config/.env` |
| `ADMIN` | Telegram ID администратора для первичного создания `config/.env` |

> Если `config/.env` уже существует на сервере, workflow не перезаписывает его.

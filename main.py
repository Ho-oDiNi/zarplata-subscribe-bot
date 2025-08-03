import asyncio
import logging
import json  # Добавлен импорт модуля json
from aiogram import Bot, Dispatcher, types
from config.bot_config import API_TOKEN, ADMIN
from utils.registers import *
from handlers import *
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Сохраняем ссылку на бота в состоянии приложения FastAPI
app.state.bot = bot

@app.get("/")
async def health_check():
    return {"status": "ok", "message": "Server is running"}

@app.post("/")
async def json_check(request: Request):
    try:
        # Логируем сырое тело запроса для отладки
        body_bytes = await request.body()
        logging.info(f"Raw request body: {body_bytes.decode('utf-8')}")
    except Exception as e:
        logging.exception("Unhandled exception in ghost_webhook")
        return {"status": "error", "detail": str(e)}
    return {"status": "ok", "message": "Server is running"}

# Добавлен декоратор для регистрации эндпоинта
@app.post("/ghost-webhook")
async def ghost_webhook(request: Request):
    try:
        # Логируем сырое тело запроса для отладки
        body_bytes = await request.body()
        logging.info(f"Raw request body: {body_bytes.decode('utf-8')}")
        
        try:
            data = await request.json()
        except json.JSONDecodeError as e:
            logging.error(f"JSON decode error: {e}")
            return {"status": "error", "detail": "Invalid JSON format"}
        
        # Логируем полученные данные
        logging.info(f"Parsed JSON data: {json.dumps(data, indent=2)}")
        
        post = data.get("post", {}).get("current", {})
        
        if post and post.get("status") == "published":
            # Получаем данные для рассылки
            tags = post.get("tags", [])
            authors = post.get("authors", [])
            
            # Извлекаем ID
            tag_slugs = [tag["slug"] for tag in tags] if tags else []
            author_slugs = [author["slug"] for author in authors] if authors else []
            
            # Получаем ID категорий и авторов
            tag_ids = get_tag_ids_by_slugs(tag_slugs)
            author_ids = get_author_ids_by_slugs(author_slugs)
            
            # Получаем подписчиков с деталями подписок
            author_subscribers, tag_subscribers, common_subs = get_subscribed_users_with_details(
                tag_ids, author_ids
            )
            
            # Рассылаем уведомления
            bot_app = request.app.state.bot
            tasks = []
            
            # Уведомления подписчикам автора
            for user_id, author_name in author_subscribers.items():
                tasks.append(
                    send_author_notification(bot_app, user_id, author_name, post["title"], post["url"])
                )
            
            # Уведомления подписчикам категорий
            for user_id, tag_names in tag_subscribers.items():
                # Фильтруем только категории статьи, на которые подписан пользователь
                user_tags = [
                    tag["name"] for tag in tags 
                    if tag["name"] in tag_names
                ]
                if user_tags:
                    tasks.append(
                        send_tag_notification(bot_app, user_id, user_tags, post["title"], post["url"])
                    )
            
            # Уведомления для общих пользователей
            for user_id, (author_name, tag_names) in common_subs.items():
                tasks.append(
                    send_author_notification(bot_app, user_id, author_name, post["title"], post["url"])
                )
            
            logging.info(f"tasks: {tasks}")
            
            # Запускаем все задачи параллельно
            if tasks:
                await asyncio.gather(*tasks)
        
        return {"status": "ok"}
    
    except Exception as e:
        logging.exception("Unhandled exception in ghost_webhook")
        return {"status": "error", "detail": str(e)}

async def run_fastapi():
    """Запуск FastAPI сервера"""
    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
    server = uvicorn.Server(config)
    await server.serve()

async def run_bot():
    """Запуск бота в режиме polling"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename="py_log.log",
        filemode="w"
    )

    dp.startup.register(start_bot_register)
    dp.shutdown.register(stop_bot_register)

    dp.include_routers(
        user_handlers.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

async def main():
    """Главная функция для параллельного запуска бота и FastAPI"""
    await asyncio.gather(
        run_fastapi(),
        run_bot()
    )

if __name__ == "__main__":
    asyncio.run(main())
from fastapi import FastAPI, Request
from aiogram import Bot
from config.bot_config import ADMIN

app = FastAPI()

@app.post("/ghost-webhook")
async def ghost_webhook(request: Request, bot: Bot):
    data = await request.json()
    post = data.get("post", {}).get("current", {})

    if post and post.get("status") == "published":
        message = (
            f"📢 Новый пост: {post['title']}\n\n"
            f"🔗 {post['url']}"
        )
        await bot.send_message(ADMIN, message)
    return {"status": "ok"}

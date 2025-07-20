import requests
from datetime import datetime, timedelta
import sqlite3
import asyncio

# Настройки Ghost CMS
GHOST_API_URL = "https://your-ghost-blog.com/ghost/api/v3/content"
GHOST_API_KEY = "your-api-key-here"
GHOST_POSTS_LIMIT = 10  # Количество постов для проверки

def get_recent_posts():
    """Получить последние посты из Ghost CMS"""
    headers = {
        "Accept-Version": "v3",
        "Authorization": f"Ghost {GHOST_API_KEY}"
    }
    
    params = {
        "limit": GHOST_POSTS_LIMIT,
        "fields": "id,title,url,created_at,published_at,updated_at,excerpt",
        "order": "published_at DESC"
    }
    
    try:
        response = requests.get(f"{GHOST_API_URL}/posts/", headers=headers, params=params)
        response.raise_for_status()
        return response.json().get('posts', [])
    except Exception as e:
        print(f"Error fetching Ghost posts: {e}")
        return []

async def check_new_posts(bot: Bot):
    """Периодическая проверка новых постов и отправка подписчикам"""
    conn = sqlite3.connect('subscriptions.db')
    cursor = conn.cursor()
    
    # Получаем время последней проверки
    cursor.execute("SELECT value FROM bot_state WHERE key = 'last_post_check'")
    last_check_row = cursor.fetchone()
    last_check = datetime.now() - timedelta(hours=1)  # По умолчанию - 1 час назад
    if last_check_row:
        last_check = datetime.fromisoformat(last_check_row[0])
    
    # Получаем новые посты
    posts = get_recent_posts()
    new_posts = [
        post for post in posts 
        if datetime.fromisoformat(post['published_at'][:-1]) > last_check
    ]
    
    if not new_posts:
        return
    
    # Обновляем время последней проверки
    new_last_check = datetime.now().isoformat()
    cursor.execute(
        "INSERT OR REPLACE INTO bot_state (key, value) VALUES (?, ?)",
        ('last_post_check', new_last_check)
    )
    conn.commit()
    
    # Отправляем новые посты подписчикам
    for post in new_posts:
        # Получаем всех подписчиков категорий/авторов этого поста
        # (Здесь нужно адаптировать под вашу логику подписок)
        
        message_text = (
            f"📢 Новый пост: {post['title']}\n\n"
            f"{post.get('excerpt', '')}\n\n"
            f"Читать полностью: {post['url']}"
        )
        
        # Пример отправки всем подписчикам (нужно адаптировать)
        cursor.execute("SELECT user_id FROM users")
        for (user_id,) in cursor.fetchall():
            try:
                await bot.send_message(user_id, message_text)
            except Exception as e:
                print(f"Error sending to user {user_id}: {e}")
    
    conn.close()

async def scheduled_post_check(bot: Bot):
    """Запуск периодической проверки"""
    while True:
        await check_new_posts(bot)
        await asyncio.sleep(300)  # Проверка каждые 5 минут
from config.bot_config import DB
import logging

def add_or_update_user(user_id):
    cursor = DB.cursor()
    
    cursor.execute('''
    INSERT OR REPLACE INTO users (id)
    VALUES (?)
    ''', (user_id,))
    
    DB.commit()
    cursor.close()

def subscribe_to_tag(user_id, target_slug):
    cursor = DB.cursor()
    
    # Check if tag exists
    cursor.execute('SELECT id FROM tags WHERE slug = ?', (target_slug,))
    tag_id = cursor.fetchone()[0]
    if not tag_id:
        cursor.close()
        return

    # Subscribe user to tag
    cursor.execute('''
    INSERT OR IGNORE INTO user_tags (user_id, tag_id)
    VALUES (?, ?)
    ''', (user_id, tag_id,))
    
    # Get tag name for response
    cursor.execute('SELECT name FROM tags WHERE id = ?', (tag_id,))
    tag_name = cursor.fetchone()[0]
    
    DB.commit()
    cursor.close()
    
    return tag_name

def subscribe_to_author(user_id, target_slug):
    cursor = DB.cursor()
    
    # Check if authors exists
    cursor.execute('SELECT id FROM authors WHERE slug = ?', (target_slug,))
    author_id = cursor.fetchone()[0]
    if not author_id:
        cursor.close()
        return

    # Subscribe user to tag
    cursor.execute('''
    INSERT OR IGNORE INTO user_authors (user_id, author_id)
    VALUES (?, ?)
    ''', (user_id, author_id,))
    
    # Get tag name for response
    cursor.execute('SELECT name FROM authors WHERE id = ?', (author_id,))
    author_name = cursor.fetchone()[0]
    
    DB.commit()
    cursor.close()
    
    return author_name

def get_tag_ids_by_slugs(slugs: list[str]) -> list[int]:
    """Возвращает ID категорий по их слагам"""
    if not slugs:
        return []
    
    cursor = DB.cursor()
    placeholders = ','.join('?' for _ in slugs)
    query = f"SELECT id FROM tags WHERE slug IN ({placeholders})"
    cursor.execute(query, slugs)
    return [row[0] for row in cursor.fetchall()]

def get_author_ids_by_slugs(slugs: list[str]) -> list[int]:
    """Возвращает ID авторов по их слагам"""
    if not slugs:
        return []
    
    cursor = DB.cursor()
    placeholders = ','.join('?' for _ in slugs)
    query = f"SELECT id FROM authors WHERE slug IN ({placeholders})"
    cursor.execute(query, slugs)
    return [row[0] for row in cursor.fetchall()]

def get_author_subscribers_with_data(author_ids: list[int]) -> dict[int, str]:
    """Возвращает {user_id: author_name} для подписчиков авторов"""
    if not author_ids:
        return {}
    
    cursor = DB.cursor()
    placeholders = ','.join('?' for _ in author_ids)
    query = f'''
        SELECT ua.user_id, a.name
        FROM user_authors ua
        JOIN authors a ON ua.author_id = a.id
        WHERE a.id IN ({placeholders})
    '''
    cursor.execute(query, author_ids)
    return {row[0]: row[1] for row in cursor.fetchall()}

def get_tag_subscribers_with_data(tag_ids: list[int]) -> dict[int, list[str]]:
    """Возвращает {user_id: [tag_names]} для подписчиков категорий"""
    if not tag_ids:
        return {}
    
    cursor = DB.cursor()
    placeholders = ','.join('?' for _ in tag_ids)
    query = f'''
        SELECT uc.user_id, c.name
        FROM user_tags uc
        JOIN tags c ON uc.tag_id = c.id
        WHERE c.id IN ({placeholders})
    '''
    cursor.execute(query, tag_ids)
    
    result = {}
    for user_id, tag_name in cursor.fetchall():
        if user_id not in result:
            result[user_id] = []
        result[user_id].append(tag_name)
    return result

def get_subscribed_users_with_details(tag_ids: list[int], author_ids: list[int]) -> tuple:
    """
    Возвращает кортеж:
    - {user_id: author_name} - только подписки на авторов
    - {user_id: [tag_names]} - только подписки на категории
    """
    author_subs = get_author_subscribers_with_data(author_ids)
    tag_subs = get_tag_subscribers_with_data(tag_ids)
    
    # Исключаем пользователей с обеими подписками
    common_users = set(author_subs.keys()) & set(tag_subs.keys())
    
    author_only = {k: v for k, v in author_subs.items() if k not in common_users}
    tag_only = {k: v for k, v in tag_subs.items() if k not in common_users}
    
    # Формируем данные для общих пользователей
    common_subs = {}
    for user_id in common_users:
        common_subs[user_id] = (author_subs[user_id], tag_subs[user_id])
    
    return author_only, tag_only, common_subs
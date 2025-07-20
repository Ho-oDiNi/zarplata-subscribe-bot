from config.bot_config import DB

def add_or_update_user(user_id):
    cursor = DB.cursor()
    
    cursor.execute('''
    INSERT OR REPLACE INTO users (user_id)
    VALUES (?)
    ''', (user_id,))
    
    DB.commit()
    cursor.close()

def subscribe_to_category(user_id, target_slug):
    cursor = DB.cursor()
    
    # Check if category exists
    cursor.execute('SELECT category_id FROM categories WHERE category_slug = ?', (target_slug,))
    category_id = cursor.fetchone()[0]
    if not category_id:
        cursor.close()
        return

    # Subscribe user to category
    cursor.execute('''
    INSERT OR IGNORE INTO user_categories (user_id, category_id)
    VALUES (?, ?)
    ''', (user_id, category_id,))
    
    # Get category name for response
    cursor.execute('SELECT category_name FROM categories WHERE category_id = ?', (category_id,))
    category_name = cursor.fetchone()[0]
    
    DB.commit()
    cursor.close()
    
    return category_name

def subscribe_to_author(user_id, target_slug):
    cursor = DB.cursor()
    
    # Check if authors exists
    cursor.execute('SELECT author_id FROM authors WHERE author_slug = ?', (target_slug,))
    author_id = cursor.fetchone()[0]
    if not author_id:
        cursor.close()
        return

    # Subscribe user to category
    cursor.execute('''
    INSERT OR IGNORE INTO user_authors (user_id, author_id)
    VALUES (?, ?)
    ''', (user_id, author_id,))
    
    # Get category name for response
    cursor.execute('SELECT author_name FROM authors WHERE author_id = ?', (author_id,))
    author_name = cursor.fetchone()[0]
    
    DB.commit()
    cursor.close()
    
    return author_name

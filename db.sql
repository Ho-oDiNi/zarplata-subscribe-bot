-- Таблица пользователей
CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

-- Таблица категорий
CREATE TABLE IF NOT EXISTS categories (
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT UNIQUE,
        category_slug TEXT UNIQUE
    )

CREATE TABLE IF NOT EXISTS user_categories (
        user_id INTEGER,
        category_id INTEGER,
        subscribe_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (user_id, category_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (category_id) REFERENCES categories(category_id)
    )

CREATE TABLE IF NOT EXISTS authors (
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        author_name TEXT UNIQUE,
        author_slug TEXT UNIQUE
    )

CREATE TABLE IF NOT EXISTS user_authors (
        user_id INTEGER,
        author_id INTEGER,
        subscribe_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (user_id, author_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (author_id) REFERENCES authors(author_id)
    )

-- Таблица: authors
INSERT INTO authors (author_id, author_name, author_slug) VALUES (1, 'Марина Нестерова', 'marina');
INSERT INTO authors (author_id, author_name, author_slug) VALUES (2, 'Андрей Алмазов', 'andriei');

-- Таблица: categories
INSERT INTO categories (category_id, category_name, category_slug) VALUES (1, 'Законы и право', 'zakony-i-pravo');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (2, 'Декрет', 'diekriet');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (3, 'Удалёнка', 'udalionka');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (4, 'Работа в офисе', 'rabota-v-ofisie');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (5, 'Руководство', 'rukovodstvo');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (6, 'Работа в команде', 'rabota-v-komandie');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (7, 'Увольнение', 'uvolnieniie');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (8, 'Фриланс', 'frilans');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (9, 'Образование', 'obrazovaniie');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (10, 'Работа и семья', 'rabota-i-siemia');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (11, 'Стажёр', 'stazhior');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (12, 'Отдых и развлечения', 'otduh-i-razvlechenia');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (13, 'Человек дела', 'chieloviek-diela');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (14, 'Бизнес', 'biznies');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (15, 'Соискателям', 'applicants');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (16, 'Работодателям', 'employers');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (17, 'Кейсы', 'cases');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (18, 'Советы по работе', 'sovetu-po-rabote');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (19, 'Новости', 'novosti');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (20, 'Студентам', 'students');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (21, 'Собеседование', 'sobiesiedovaniie');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (22, 'Ищу работу', 'ishchu-rabotu');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (23, 'Ищу сотрудника', 'ishchu-sotrudnika');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (24, 'Карьерные советы', 'kariernyie-soviety');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (25, 'Полезно', 'poliezno');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (26, 'Резюме', 'rieziumie');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (27, 'Интервью', 'interview');
INSERT INTO categories (category_id, category_name, category_slug) VALUES (28, 'Круглый стол', 'krughlyi-stol');

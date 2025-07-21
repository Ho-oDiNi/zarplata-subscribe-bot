-- Таблица пользователей
CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

-- Таблица категорий
CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        slug TEXT UNIQUE
    )

CREATE TABLE IF NOT EXISTS user_categories (
        user_id INTEGER,
        category_id INTEGER,
        subscribe_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (user_id, category_id),
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )

CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        slug TEXT UNIQUE
    )

CREATE TABLE IF NOT EXISTS user_authors (
        user_id INTEGER,
        author_id INTEGER,
        subscribe_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (user_id, author_id),
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (author_id) REFERENCES authors(id)
    )
    
-- Таблица: authors
INSERT INTO authors (id, name, slug) VALUES (1, 'Марина Нестерова', 'marina');
INSERT INTO authors (id, name, slug) VALUES (2, 'Андрей Алмазов', 'andriei');

-- Таблица: categories
INSERT INTO categories (id, name, slug) VALUES (1, 'Законы и право', 'zakony-i-pravo');
INSERT INTO categories (id, name, slug) VALUES (2, 'Декрет', 'diekriet');
INSERT INTO categories (id, name, slug) VALUES (3, 'Удалёнка', 'udalionka');
INSERT INTO categories (id, name, slug) VALUES (4, 'Работа в офисе', 'rabota-v-ofisie');
INSERT INTO categories (id, name, slug) VALUES (5, 'Руководство', 'rukovodstvo');
INSERT INTO categories (id, name, slug) VALUES (6, 'Работа в команде', 'rabota-v-komandie');
INSERT INTO categories (id, name, slug) VALUES (7, 'Увольнение', 'uvolnieniie');
INSERT INTO categories (id, name, slug) VALUES (8, 'Фриланс', 'frilans');
INSERT INTO categories (id, name, slug) VALUES (9, 'Образование', 'obrazovaniie');
INSERT INTO categories (id, name, slug) VALUES (10, 'Работа и семья', 'rabota-i-siemia');
INSERT INTO categories (id, name, slug) VALUES (11, 'Стажёр', 'stazhior');
INSERT INTO categories (id, name, slug) VALUES (12, 'Отдых и развлечения', 'otduh-i-razvlechenia');
INSERT INTO categories (id, name, slug) VALUES (13, 'Человек дела', 'chieloviek-diela');
INSERT INTO categories (id, name, slug) VALUES (14, 'Бизнес', 'biznies');
INSERT INTO categories (id, name, slug) VALUES (15, 'Соискателям', 'applicants');
INSERT INTO categories (id, name, slug) VALUES (16, 'Работодателям', 'employers');
INSERT INTO categories (id, name, slug) VALUES (17, 'Кейсы', 'cases');
INSERT INTO categories (id, name, slug) VALUES (18, 'Советы по работе', 'sovetu-po-rabote');
INSERT INTO categories (id, name, slug) VALUES (19, 'Новости', 'novosti');
INSERT INTO categories (id, name, slug) VALUES (20, 'Студентам', 'students');
INSERT INTO categories (id, name, slug) VALUES (21, 'Собеседование', 'sobiesiedovaniie');
INSERT INTO categories (id, name, slug) VALUES (22, 'Ищу работу', 'ishchu-rabotu');
INSERT INTO categories (id, name, slug) VALUES (23, 'Ищу сотрудника', 'ishchu-sotrudnika');
INSERT INTO categories (id, name, slug) VALUES (24, 'Карьерные советы', 'kariernyie-soviety');
INSERT INTO categories (id, name, slug) VALUES (25, 'Полезно', 'poliezno');
INSERT INTO categories (id, name, slug) VALUES (26, 'Резюме', 'rieziumie');
INSERT INTO categories (id, name, slug) VALUES (27, 'Интервью', 'interview');
INSERT INTO categories (id, name, slug) VALUES (28, 'Круглый стол', 'krughlyi-stol');

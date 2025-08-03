-- Таблица пользователей
CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

-- Таблица категорий
CREATE TABLE IF NOT EXISTS tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        slug TEXT UNIQUE
    )

CREATE TABLE IF NOT EXISTS user_tags (
        user_id INTEGER,
        tag_id INTEGER,
        subscribe_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (user_id, tag_id),
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (tag_id) REFERENCES tags(id)
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

-- Таблица: tags
INSERT INTO tags (id, name, slug) VALUES (1, 'Законы и право', 'zakony-i-pravo');
INSERT INTO tags (id, name, slug) VALUES (2, 'Декрет', 'diekriet');
INSERT INTO tags (id, name, slug) VALUES (3, 'Удалёнка', 'udalionka');
INSERT INTO tags (id, name, slug) VALUES (4, 'Работа в офисе', 'rabota-v-ofisie');
INSERT INTO tags (id, name, slug) VALUES (5, 'Руководство', 'rukovodstvo');
INSERT INTO tags (id, name, slug) VALUES (6, 'Работа в команде', 'rabota-v-komandie');
INSERT INTO tags (id, name, slug) VALUES (7, 'Увольнение', 'uvolnieniie');
INSERT INTO tags (id, name, slug) VALUES (8, 'Фриланс', 'frilans');
INSERT INTO tags (id, name, slug) VALUES (9, 'Образование', 'obrazovaniie');
INSERT INTO tags (id, name, slug) VALUES (10, 'Работа и семья', 'rabota-i-siemia');
INSERT INTO tags (id, name, slug) VALUES (11, 'Стажёр', 'stazhior');
INSERT INTO tags (id, name, slug) VALUES (12, 'Отдых и развлечения', 'otduh-i-razvlechenia');
INSERT INTO tags (id, name, slug) VALUES (13, 'Человек дела', 'chieloviek-diela');
INSERT INTO tags (id, name, slug) VALUES (14, 'Бизнес', 'biznies');
INSERT INTO tags (id, name, slug) VALUES (15, 'Соискателям', 'applicants');
INSERT INTO tags (id, name, slug) VALUES (16, 'Работодателям', 'employers');
INSERT INTO tags (id, name, slug) VALUES (17, 'Кейсы', 'cases');
INSERT INTO tags (id, name, slug) VALUES (18, 'Советы по работе', 'sovetu-po-rabote');
INSERT INTO tags (id, name, slug) VALUES (19, 'Новости', 'novosti');
INSERT INTO tags (id, name, slug) VALUES (20, 'Студентам', 'students');
INSERT INTO tags (id, name, slug) VALUES (21, 'Собеседование', 'sobiesiedovaniie');
INSERT INTO tags (id, name, slug) VALUES (22, 'Ищу работу', 'ishchu-rabotu');
INSERT INTO tags (id, name, slug) VALUES (23, 'Ищу сотрудника', 'ishchu-sotrudnika');
INSERT INTO tags (id, name, slug) VALUES (24, 'Карьерные советы', 'kariernyie-soviety');
INSERT INTO tags (id, name, slug) VALUES (25, 'Полезно', 'poliezno');
INSERT INTO tags (id, name, slug) VALUES (26, 'Резюме', 'rieziumie');
INSERT INTO tags (id, name, slug) VALUES (27, 'Интервью', 'interview');
INSERT INTO tags (id, name, slug) VALUES (28, 'Круглый стол', 'krughlyi-stol');

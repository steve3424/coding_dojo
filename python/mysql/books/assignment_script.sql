use books_db;

-- 1. Create 5 different authors
#insert into authors (name, created_at, updated_at)
#values("Jane Austen", now(), now()),
#      ("Emily Dickinson", now(), now()),
#      ("Fyodor Dostoevsky", now(), now()),
#      ("William Shakespeare", now(), now()),
#      ("Lau Tzu", now(), now());

-- 2. Create 5 books
#insert into books (title, num_pages, created_at, updated_at)
#values("C Sharp", 720, now(), now()),
#      ("Java", 720, now(), now()),
#      ("Python", 100, now(), now()),
#      ("C", 4, now(), now()),
#      ("SQL", 190, now(), now());

-- 3. Change book title
#update books
#set title="C#"
#where title="C Sharp";

-- 5. First author favorite first 2 books
#insert into favorites (author_id, book_id)
#values((select min(id) from authors), (select min(id) from books))
#      ((select min(id) from authors), (select min(id) from books) + 1);

-- 6. Second author favorite first 3 books
#insert into favorites (author_id, book_id)
#values((select min(id) from authors) + 1, (select min(id) from books)),
#      ((select min(id) from authors) + 1, (select min(id) from books) + 1),
#      ((select min(id) from authors) + 1, (select min(id) from books) + 2);

-- 7. Third author favorite first 4 books
#insert into favorites (author_id, book_id)
#values((select min(id) from authors) + 2, (select min(id) from books)),
#      ((select min(id) from authors) + 2, (select min(id) from books) + 1),
#      ((select min(id) from authors) + 2, (select min(id) from books) + 2),
#      ((select min(id) from authors) + 2, (select min(id) from books) + 3);

-- 7. Fourth author favorite all books
#insert into favorites (author_id, book_id)
#select (select min(id) from authors) + 3, id from books;

-- 8. All authors who favorited 3rd book
#select authors.name, books.id, books.title
#from authors
#join favorites
#on favorites.author_id = authors.id
#join books
#on book_id = books.id
#where books.id = 3;

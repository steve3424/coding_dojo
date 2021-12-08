insert into users (first_name, last_name, email, created_at, updated_at)
values ("fname_1", "lname_1", "email_1", now(), now()),
       ("fname_2", "lname_2", "email_2", now(), now()),
       ("fname_3", "lname_3", "email_3", now(), now());

select * from users;

select * from users
where email="email_1";

select * from users
where id=(select max(id) from users);

update users
set last_name="Pancakes"
where id=3;

delete from users
where id=2;

select * from users
order by first_name;

select * from users
order by first_name desc;

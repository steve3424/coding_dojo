set SQL_SAFE_UPDATES = 0;

-- 1. Create 3 new dojos
INSERT INTO dojos (name, created_at, updated_at)
VALUES ("dojo_1", NOW(), NOW()),
	   ("dojo_2", NOW(), NOW()),
	   ("dojo_3", NOW(), NOW());

-- 2. Delete 3 dojos just created
DELETE FROM dojos;

-- 3. Create 3 more dojos
INSERT INTO dojos (name, created_at, updated_at)
VALUES ("dojo_1", NOW(), NOW()),
	   ("dojo_2", NOW(), NOW()),
	   ("dojo_3", NOW(), NOW());

-- 4. Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
SELECT "ninja_1_first", "ninja_1_last", 21, NOW(), NOW(), id
FROM dojos
WHERE dojos.name = "dojo_1";

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
SELECT "ninja_2_first", "ninja_2_last", 22, NOW(), NOW(), id
FROM dojos
WHERE dojos.name = "dojo_1";

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
SELECT "ninja_3_first", "ninja_3_last", 23, NOW(), NOW(), id
FROM dojos
WHERE dojos.name = "dojo_1";

-- 4. Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
SELECT "ninja_4_first", "ninja_4_last", 21, NOW(), NOW(), id
FROM dojos
WHERE dojos.name = "dojo_2";

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
SELECT "ninja_5_first", "ninja_5_last", 22, NOW(), NOW(), id
FROM dojos
WHERE dojos.name = "dojo_2";

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
SELECT "ninja_6_first", "ninja_6_last", 23, NOW(), NOW(), id
FROM dojos
WHERE dojos.name = "dojo_2";

-- 5. Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
SELECT "ninja_7_first", "ninja_7_last", 21, NOW(), NOW(), id
FROM dojos
WHERE dojos.name = "dojo_3";

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
SELECT "ninja_8_first", "ninja_8_last", 22, NOW(), NOW(), id
FROM dojos
WHERE dojos.name = "dojo_3";

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
SELECT "ninja_9_first", "ninja_9_last", 23, NOW(), NOW(), id
FROM dojos
WHERE dojos.name = "dojo_3";

-- 6. Retrieve all ninjas from first dojo
SELECT ninjas.first_name, ninjas.last_name, dojos.name
FROM ninjas
JOIN dojos
ON ninjas.dojo_id = dojos.id
WHERE dojos.id = (SELECT MIN(id) FROM dojos);

-- 7. Retrieve all ninjas from the last dojo
SELECT ninjas.first_name, ninjas.last_name, dojos.name
FROM ninjas
JOIN dojos
ON ninjas.dojo_id = dojos.id
WHERE dojos.id = (SELECT MAX(id) FROM dojos);

-- 8. Retrieve the last ninja's dojo
SELECT dojos.name, ninjas.first_name, ninjas.last_name
FROM dojos
JOIN ninjas
ON ninjas.dojo_id = dojos.id
WHERE ninjas.id = (SELECT MAX(id) FROM ninjas);
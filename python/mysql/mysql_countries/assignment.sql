use world;


-- -- Query 1
-- SELECT countries.name, languages.language, languages.percentage
-- FROM languages
-- JOIN countries
-- ON languages.country_id = countries.id
-- WHERE languages.language = "Slovene"
-- ORDER BY languages.percentage DESC;
-- 
-- -- Query 2
-- SELECT countries.name, COUNT(cities.id) as num_cities
-- FROM countries
-- JOIN cities
-- ON countries.id = cities.country_id
-- GROUP BY countries.name
-- ORDER BY COUNT(cities.country_id) DESC;
-- 
-- -- Query 3
-- SELECT countries.name, cities.name, cities.population
-- FROM countries
-- JOIN cities
-- ON countries.id = cities.country_id
-- WHERE cities.population > 500000
-- AND 
-- countries.name = "Mexico"
-- ORDER BY cities.population DESC;
-- 
-- -- Query 4
-- SELECT countries.name, languages.language, languages.percentage
-- FROM countries
-- JOIN languages
-- on countries.id = languages.country_id
-- where languages.percentage > 89
-- order by languages.percentage desc;
-- 
-- -- Query 5
-- select name, surface_area, population
-- from countries
-- where surface_area < 501
-- and
-- population > 100000;
-- 
-- -- Query 6
-- select name, government_form, capital, life_expectancy
-- from countries
-- where government_form = "Constitutional Monarchy"
-- and capital > 200
-- and life_expectancy > 75;
-- 
-- -- Query 7
-- select countries.name, cities.name, cities.district, cities.population
-- from countries
-- join cities
-- on countries.id = cities.country_id
-- where cities.district = "Buenos Aires"
-- and cities.population > 500000;
-- 
-- -- Query 8
-- select region, count(region)
-- from countries
-- group by countries.region
-- order by count(countries.region) desc;

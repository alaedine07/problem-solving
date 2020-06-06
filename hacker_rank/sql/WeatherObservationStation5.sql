select city, length(city) From station
order by length(city), city
limit 1; /*because only one city */ 

select city, length(city) from station
order by length(city) DESC, city
limit 1;

-- https://school.programmers.co.kr/learn/courses/30/lessons/157341
-- 코드를 입력하세요
select distinct(r.car_id)
from car_rental_company_rental_history r
where r.car_id in (select car_id from car_rental_company_car where car_type="세단")
and start_date between '2022-10-01' and '2022-10-31' order by r.car_id desc;
-- REST_INFO 테이블에서 음식종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류, ID, 식당 이름, 즐겨찾기수를 조회하는 SQL문을 작성해주세요. 이때 결과는 음식 종류를 기준으로 내림차순 정렬해주세요.
-- 코드를 입력하세요
SELECT ri.food_type, ri.rest_id, ri.rest_name, ri.favorites
from rest_info ri join (select food_type, max(favorites) as max_fav from rest_info group by food_type) rf
on ri.food_type = rf.food_type and ri.favorites = rf.max_fav
order by ri.food_type desc;
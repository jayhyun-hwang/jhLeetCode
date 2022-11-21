-- https://school.programmers.co.kr/learn/courses/30/lessons/131116

SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
AND PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT GROUP BY CATEGORY)
GROUP BY CATEGORY
ORDER BY MAX_PRICE DESC

--- OR

select pr.category, pr.price as max_price, pr.product_name 
from (
    SELECT *, RANK() OVER(PARTITION BY CATEGORY ORDER BY PRICE DESC) PR
        FROM FOOD_PRODUCT
        WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
) pr where pr.pr = 1 order by max_price desc;

-- select id, amount, rank() over (order by amount desc) as ranking 
-- from ex_card

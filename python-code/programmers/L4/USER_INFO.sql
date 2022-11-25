-- https://school.programmers.co.kr/learn/courses/30/lessons/131532

-- 한 사람이 여러개의 상품을 구매할 경우, 여러번 count 되므로 distinct를 사용해야한다

-- 코드를 입력하세요
SELECT
    year(os.sales_date) as YEAR,
    month(os.sales_date) as MONTH,
    ui.gender as GENDER,
    count(distinct ui.user_id) as USERS
from user_info ui
    join online_sale os on ui.user_id = os.user_id
where ui.gender is not null
GROUP BY
    YEAR,
    MONTH,
    ui.gender -- having ui.gender is not null
order by YEAR, MONTH, GENDER asc;

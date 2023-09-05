-- https://school.programmers.co.kr/learn/courses/30/lessons/133027
-- 코드를 입력하세요

SELECT h.flavor
from first_half h
    join (
        select
            flavor,
            sum(total_order) as "total"
        from july
        group by
            flavor
    ) j on h.flavor = j.flavor
order by (h.total_order + j.total) desc
limit 3;
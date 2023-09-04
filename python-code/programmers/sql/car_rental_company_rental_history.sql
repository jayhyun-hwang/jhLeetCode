-- https://school.programmers.co.kr/learn/courses/30/lessons/157340
-- 코드를 입력하세요

select
    r.car_id,
    case
        when (sum(r.occupy) > 0) then "대여중"
        else "대여 가능"
    end as availability
from (
        select
            car_id,
            case
                when (
                    start_date <= '2022-10-16'
                    and end_date >= '2022-10-16'
                ) then 1
                else 0
            end as "occupy"
        from
            car_rental_company_rental_history
    ) r
group by r.car_id
order by r.car_id desc;
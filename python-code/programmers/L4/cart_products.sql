-- https://school.programmers.co.kr/learn/courses/30/lessons/62284

SELECT y.cart_id
from (
        select cart_id
        from cart_products
        where name = 'Yogurt'
    ) y
    join (
        select cart_id
        from cart_products
        where
            name = 'Milk'
    ) m on y.cart_id = m.cart_id
order by y.cart_id;
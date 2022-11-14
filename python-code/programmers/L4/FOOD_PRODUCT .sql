-- 코드를 입력하세요
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, SUM(p.price * o.amount) as TOTAL_SALES
    from food_product p join food_order o on p.product_id = o.product_id
    where year(o.produce_date) = 2022 and month(o.produce_date) = 5
    group by p.product_id, p.product_name
    order by TOTAL_SALES desc, p.product_id asc;
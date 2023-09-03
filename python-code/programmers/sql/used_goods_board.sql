-- https://school.programmers.co.kr/learn/courses/30/lessons/164668
-- 코드를 입력하세요
select u.USER_ID, u.NICKNAME, b.TOTAL_SALES
from (select writer_id, sum(price) as total_sales from used_goods_board where status="DONE" group by writer_id) b
join used_goods_user u on b.writer_id=u.user_id
where b.total_sales >= 700000 order by b.total_sales;
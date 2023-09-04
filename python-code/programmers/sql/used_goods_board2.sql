-- https://school.programmers.co.kr/learn/courses/30/lessons/164670
-- 코드를 입력하세요

select
    u.user_id,
    u.nickname,
    concat(
        u.city,
        ' ',
        u.street_address1,
        ' ',
        u.street_address2
    ) as "전체주소",
    concat(
        LEFT(u.tlno, 3),
        '-',
        SUBSTRING(u.tlno, 4, 4),
        '-',
        RIGHT(u.tlno, 4)
    ) as "전화번호"
from (
        select
            writer_id,
            count(writer_id) as count
        from used_goods_board
        group by writer_id
        having count >= 3
    ) b
    join used_goods_user u on b.writer_id = u.user_id
order by u.user_id desc;
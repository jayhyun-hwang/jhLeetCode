-- 이 서비스에서는 공간을 둘 이상 등록한 사람을 "헤비 유저"라고 부릅니다. 헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회하는 SQL문을 작성해주세요.
-- 코드를 입력하세요
SELECT p.id, p.name, p.host_id
from places p 
join (select host_id, count(host_id) as cnt from places group by host_id) h
on p.host_id = h.host_id where h.cnt >= 2
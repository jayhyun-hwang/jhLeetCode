-- 천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
-- 코드를 입력하세요
SELECT ao.animal_id, ao.name
from animal_outs ao left join animal_ins ai on ao.animal_id = ai.animal_id
where ai.animal_id is null
-- 코드를 입력하세요

SELECT
    i.ANIMAL_ID,
    i.ANIMAL_TYPE,
    i.NAME
FROM ANIMAL_INS i
    JOIN ANIMAL_OUTS o ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE
    i.SEX_UPON_INTAKE NOT IN (
        'Spayed Female',
        'Neutered Male'
    )
    AND o.SEX_UPON_OUTCOME IN (
        'Spayed Female',
        'Neutered Male'
    )
ORDER BY i.ANIMAL_ID;
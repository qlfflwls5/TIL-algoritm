--오랜 기간 보호한 동물(2)
--
--입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.

SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS AS A INNER JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY DATEDIFF(A.DATETIME, B.DATETIME)
LIMIT 2
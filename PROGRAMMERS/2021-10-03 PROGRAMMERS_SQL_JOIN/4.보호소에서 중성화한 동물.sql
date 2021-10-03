--보호소에서 중성화한 동물

--보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다.
--보호소에 들어올 당시에는 중성화1되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.

SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS as A INNER JOIN ANIMAL_OUTS as B
ON A.ANIMAL_ID = B.ANIMAL_ID
-- 첫 번째 방법
-- WHERE (SUBSTR(A.SEX_UPON_INTAKE, 1, INSTR(A.SEX_UPON_INTAKE, ' ')-1) IN ('Intact')) AND
-- (SUBSTR(B.SEX_UPON_OUTCOME, 1, INSTR(B.SEX_UPON_OUTCOME, ' ')-1) IN ('Spayed', 'Neutered'))
-- 두 번째 방법 NOT LIKE를 쓸 수도 있다. NOT LIKE 'Intact%'
WHERE A.SEX_UPON_INTAKE LIKE 'Intact%' AND (B.SEX_UPON_OUTCOME LIKE 'Spayed%' OR B.SEX_UPON_OUTCOME LIKE 'Neutered%')
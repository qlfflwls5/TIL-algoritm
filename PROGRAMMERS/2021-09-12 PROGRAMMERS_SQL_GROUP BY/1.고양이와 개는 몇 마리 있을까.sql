--ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며,
--ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일,
--보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.
--
--동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.

-- AS를 통해 집계함수의 칼럼명을 정해줄 수 있다.
-- SQL문의 순서는 SELECT - FROM - WHERE - GROUP BY - HAVING - ORDER BY
-- 각 그룹에 대해 정렬을 한 상태로 하고 싶다면, SELECT * FROM (SELECT * FROM 테이블명 ORDER BY 필드명) GROUP BY 필드명
-- ORDER BY 정렬 시 원하는 임의 순서가 있다면 ORDER BY FIELD(필드명, 값1, 값2, ...)
SELECT ANIMAL_TYPE, COUNT(*) AS count FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY FIELD(ANIMAL_TYPE, 'Cat', 'Dog')
--중복 아이디 제거하기
--ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며,
--ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일,
--보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.
--
--동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.

-- DISTINCT는 안쪽에 써준다. NULL이 아닌 것은 IS NOT NULL. 근데 이건 DISTINCT에 NAME이라는 칼럼이 들어가 자동으로 NULL이 제거된다고 한다.
SELECT COUNT(DISTINCT NAME) count FROM ANIMAL_INS WHERE NAME IS NOT NULL
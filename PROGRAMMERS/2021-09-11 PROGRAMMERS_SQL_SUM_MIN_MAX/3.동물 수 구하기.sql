--동물 수 구하기
--ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며,
--ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일,
--보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.
--
--동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.

-- 바로 뒤에 칼럼의 이름을 지정해줄 수 있다.
SELECT COUNT(*) count FROM ANIMAL_INS
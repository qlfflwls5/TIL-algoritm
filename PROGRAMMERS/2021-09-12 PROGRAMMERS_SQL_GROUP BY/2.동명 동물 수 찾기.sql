--동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요.
--이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.

-- 조건에 해당하는 것들만(이름이 있는 것) 그룹에 넣고 싶으므로 GROUP BY에 앞서 WHERE에서 IS NOT NULL로 처리
-- 두 개 이상인 그룹만 가져오고 싶으므로 HAVING COUNT(*) >= 2
SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMAL_INS WHERE NAME IS NOT NULL GROUP BY NAME HAVING COUNT(*) >= 2 ORDER BY NAME
--보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다.
--09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요.
--이때 결과는 시간대 순으로 정렬해야 합니다.

-- HOUR(DATETIME)을 사용하면 시간만 받아올 수 있다.
SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT FROM ANIMAL_OUTS GROUP BY HOUR HAVING HOUR BETWEEN 9 AND 19 ORDER BY HOUR
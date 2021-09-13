--보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다.
--0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

-- 1번째 방법
-- SET과 @변수명을 사용해서 변수를 선언할 수 있다.
-- :=를 통해 값을 대입한다.
-- SELECT (@hour := @hour + 1) 을 통해 0부터 시작하는 @hour들에 대해 select를 실행할 수 있고, 맨 마지막의 WHERE를 통해서 종료조건을 정한다.
-- COUNT는 각 @hour에 대한 COUNT를 구해야 하므로 새로운 SELECT문을 내부에 써준다.
SET @hour := -1;

SELECT (@hour := @hour + 1) AS HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) AS COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23


--2번째 방법
-- WITH RECURSIVE 가상테이블명 AS (
--    SELECT 0 as HOUR  //  초기값 설정
--    UNION  //  아래의 쿼리들을 합칠 것(재귀될)
--    SELECT HOUR + 1 FROM 가상테이블명 WHERE HOUR < 23  //  유니온 할 쿼리들, WHERE로 종료 조건 설정
-- )
-- 위 코드를 통해 0 ~ 23까지의 값을 갖는 가상 테이블 완성. 여기에 ANIMAL_OUTS를 LEFT JOIN할 것
-- 조인 과정에서 시간을 비교하게 되며 만약 없는 시간이라면 LEFT JOIN이기 때문에 NULL이 될 것. 이를 카운트하면 0이 된다.
WITH RECURSIVE TIME AS  (
    SELECT 0 as HOUR
    UNION
    SELECT HOUR + 1 FROM TIME WHERE HOUR < 23
)

SELECT HOUR, COUNT(ANIMAL_OUTS.DATETIME) AS COUNT
FROM TIME LEFT JOIN ANIMAL_OUTS ON TIME.HOUR = HOUR(ANIMAL_OUTS.DATETIME)
GROUP BY HOUR
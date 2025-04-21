# 11 : 52

# 평균 길이가 33cm 이상인 물고기들을 종류별로 분류하여 잡은 수, 최대 길이, 물고기의 종류를 출력
# 물고기 종류에 대해 오름차순으로 정렬, 10cm이하의 물고기들은 10cm로 취급하고, 평균길이 구하기
# 근데 출력되는값은 최대 길이인데, 평균길이가 왜필요하지?

# select count(id) as FISH_COUNT, length as MAX_LENGTH, FISH_TYPE
# from fish_info
# where max(length)
# group by fish_type
# order by FISH_TYPE asc

SELECT 
COUNT(*) AS FISH_COUNT,
MAX(COALESCE(LENGTH, 10)) AS MAX_LENGTH,
FISH_TYPE

FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING AVG(COALESCE(LENGTH, 10)) >= 33
ORDER BY FISH_TYPE ASC;

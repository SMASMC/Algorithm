-- 코드를 입력하세요
SELECT datetime
from animal_ins
where datetime = (select min(datetime) from animal_ins)
# order by datetime asc # 맞는지 확인하기 위한 시험 쿼리

# 2013-10-14 15:38:00
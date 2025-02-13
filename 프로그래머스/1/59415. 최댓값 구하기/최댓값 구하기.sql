-- 코드를 입력하세요
SELECT datetime as '시간'
FROM animal_ins
where datetime = (select max(DATETIME) from animal_ins)

# 2018-02-03 10:40:00
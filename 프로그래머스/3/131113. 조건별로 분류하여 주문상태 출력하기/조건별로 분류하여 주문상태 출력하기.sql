# 테이블에서 2022년 5월 1일을 기준으로 정보를 출력하는 쿼리 작성
# OUT_DATE 를 기준으로 2022년 5월 1일까지 출고완료로 출력,
# 이 후 날짜는 출고대기
# 날짜가 없으면 출고미정
# case 문을 사용하면 끝날 것이다.
select order_id, product_id, date_format(out_date, '%Y-%m-%d') as out_date, 
case 
when OUT_DATE <= '2022-05-01' then '출고완료'
when out_date > '2022-05-01' then '출고대기'
else '출고미정'
end as '출고여부'
from FOOD_ORDER
order by order_id asc
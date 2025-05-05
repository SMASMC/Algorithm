-- 코드를 입력하세요
# CAR_RENTAL_COMPANY_RENTAL_HISTORY테이블에서 평균 대여 기간이 7일 이상
# 자동차들의 자동차 id와 평균 대여 기간
# 소수점 두번째 자리에서 반올림하고, 결과는 평균 대여 기간을 기준으로 내림차순 정렬
# 자동차ID까지 기준으로 내림차순 정렬

# DATEDIFF 두 날짜간의 차이를 구하는 함수
select car_id, round(avg(DATEDIFF( end_date, start_date)) + 1,1) as AVERAGE_DURATION
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
# 평균 대여 기간이 7일 이상
having AVERAGE_DURATION >=7
# 결과는 평균 대여 기간을 기준으로 내림차순 정렬, 같으면 자동차 id까지 기준으로 내림차순 정렬
order by AVERAGE_DURATION desc, car_id desc
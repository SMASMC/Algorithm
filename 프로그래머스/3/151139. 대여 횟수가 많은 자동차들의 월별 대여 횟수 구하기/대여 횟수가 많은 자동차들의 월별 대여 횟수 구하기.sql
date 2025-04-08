# 16 : 57
# 재시도 필요
select month(START_DATE) as month,
car_id
, count(car_id) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where (month(start_date) >= 8 and month(start_date) <= 10)
and car_id in (select car_id 
               from CAR_RENTAL_COMPANY_RENTAL_HISTORY
               where (month(start_date) >= 8 and month(start_date) <= 10)
               group by car_id
               having count(car_id) >= 5
              )
group by month(START_DATE), car_id
having records >=1
order by month asc, car_id desc;

# 총 대여 횟수가 5회 이상이인것과
# 해당 월동안에 자동차 ID 별 총 대여 횟수를 출력하라
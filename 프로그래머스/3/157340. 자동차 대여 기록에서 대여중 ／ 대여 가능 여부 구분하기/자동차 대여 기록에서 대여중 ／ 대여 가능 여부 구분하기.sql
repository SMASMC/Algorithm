# # 21 : 39
# SELECT CAR_ID, 
# CASE
#     WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE THEN '대여중'
#     ELSE '대여가능'
# END AS AVAILABILITY
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# GROUP BY CAR_ID
# ORDER BY CAR_ID DESC
# # END_DATE에서 값이 2022/10/16이상이라면, 대여중, 아니라면 대여가능
# # SELECT * FROM table_a WHERE DATE(create_dt) >= '2020-01-01' AND DATE(a.create_dt) <= '2020-12-31';

SELECT DISTINCT CAR_ID,
       CASE
           WHEN CAR_ID IN (
               SELECT CAR_ID
               FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
               WHERE '2022-10-16' BETWEEN START_DATE AND END_DATE
           ) THEN '대여중'
           ELSE '대여 가능'
       END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
ORDER BY CAR_ID DESC;

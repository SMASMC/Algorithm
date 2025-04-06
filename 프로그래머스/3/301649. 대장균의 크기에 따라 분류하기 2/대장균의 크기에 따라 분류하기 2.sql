# # 23 : 17
# # 상위 0% ~ 25% 를 'CRITICAL', 26% ~ 50% 를 'HIGH', 51% ~ 75% 를 'MEDIUM', 76% ~ 100% 를 'LOW' 라고 분류
# select id, SIZE_OF_COLONY,
SELECT id,
       CASE 
           WHEN colony_percent =1 THEN 'CRITICAL'
           WHEN colony_percent=2 then'HIGH'
           WHEN colony_percent =3 THEN 'MEDIUM'
           ELSE 'LOW'
       END AS colony_name
FROM (
    SELECT id, SIZE_OF_COLONY,
           ntile(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS colony_percent
    FROM ecoli_data
) AS sub
order by id asc
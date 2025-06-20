# ONLINE_SALE 테이블과 OFFLINE_SALE 테이블에서 2022년 3월의 오프라인/온라인 상품 판매 데이터의 판매 날짜, 상품ID, 유저ID, 판매량을 출력하는 SQL문을 작성해주세요

select date_format(sales_date, '%Y-%m-%d') as sales_date, product_id, user_id, sales_amount
from (select sales_date, product_id, user_id, sales_amount
from online_sale
union all 
select sales_date, product_id, NULL as user_id, sales_amount
from offline_sale) as all_sale
where sales_date >='2022-03-01' and sales_date <= '2022-03-31'
order by sales_date asc, product_id asc,user_id asc
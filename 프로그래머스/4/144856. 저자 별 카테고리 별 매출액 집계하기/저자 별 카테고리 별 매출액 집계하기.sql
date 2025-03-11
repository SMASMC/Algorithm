# 23 : 02
# 2022년 1월의 도서 판매 데이터를 기준으로 저자 별, 카테고리 별
# 매출액 (TOTAL_SALES = 판매량 * 판매가)에 따라 각 컬럼을 출력,
# 결과는 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬

SELECT b.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, SUM(s.SALES * b.PRICE) as TOTAL_SALES
FROM (BOOK as b inner join AUTHOR as a on b.AUTHOR_ID = a.AUTHOR_ID)
inner join BOOK_SALES as s on b.BOOK_ID = s.BOOK_ID
WHERE s.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY a.AUTHOR_NAME, b.CATEGORY, b.AUTHOR_ID
order by b.AUTHOR_ID asc , b.category desc
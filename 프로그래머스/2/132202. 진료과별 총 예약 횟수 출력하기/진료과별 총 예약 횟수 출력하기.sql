-- 코드를 입력하세요
SELECT MCDP_CD as '진료과코드', count(MCDP_CD) as '5월예약건수'
from APPOINTMENT 
WHERE APNT_YMD BETWEEN '2022-05-01' AND '2022-05-31' 
group by MCDP_CD
order by count(MCDP_CD) asc, MCDP_CD asc
# MCDP_CD를 group by를 진행 후, count로 5월 예약 건수 주면 될듯?
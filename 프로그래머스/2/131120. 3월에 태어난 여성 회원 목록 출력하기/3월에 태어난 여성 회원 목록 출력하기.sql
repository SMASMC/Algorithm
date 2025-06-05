# MEMBER_PROFILE 테이블에서 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일을 조회하는 SQL문을 작성해주세요.
# 이때 전화번호가 NULL인 경우는 출력대상에서 제외시켜 주시고, 결과는 회원ID를 기준으로 오름차순 정렬

-- 문제를 보면 date로 조회하고, null인것을 빼면 됨
# 주의사항
# DATE_OF_BIRTH의 데이트 포맷이 예시와 동일해야 정답처리 됩니다.
select MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from member_profile
where month(DATE_OF_BIRTH) = 3
and TLNO is not null
and gender = 'w'
order by member_id asc
-- 코드를 작성해주세요

# 잡은 물고기의 길이가 10cm이하면 length가 null이다.
# fish_info테이블에서 가장 큰 물고기 10마리의 id와 length를 출력하는 sql을 작성하라
# 길이 기준으로 내림차순, 같다면 id에 대해 오름차순 정렬

select id, length from fish_info
order by length desc, id asc
limit 10
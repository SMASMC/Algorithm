# 잡은 물고기의 길이가 10cm이하이면 length가 null,
# null인 것을 count하는 쿼리 작성

select count(id) as fish_count from fish_info where length is null
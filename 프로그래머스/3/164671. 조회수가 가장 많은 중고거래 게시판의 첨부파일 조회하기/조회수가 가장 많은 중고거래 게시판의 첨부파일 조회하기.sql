# USED_GOODS_BOARD 와 USED_GOODS_FILE에서 조회수가 가장 높은 중고거래 게시물에 대한
# 경로를 조회하는 쿼리 작성 /home/grep/src/를 붙여서 출력해주세요
# 최종 경로 /home/grep/src/ board_id / file_id / file_name / file_ext
SELECT concat('/home/grep/src/', file.board_id, '/', file.file_id,
             file.file_name, file.file_ext) as file_path
from USED_GOODS_BOARD as board
left join USED_GOODS_file as file
on board.board_id = file.board_id
# 조건으로 views의 값이 제일 큰 row를 출력하여 그거에 대한 경로를 출력하겠습니다.
where board.views = (select max(views) from USED_GOODS_BOARD)
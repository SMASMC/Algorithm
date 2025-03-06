# 21 : 35
# USED_GOODS_BOARD와 USED_GOODS_USER 에서 게시물 3건 이상 등록한 사용자의
# 사용자 ID, 닉네임, 전체주소, 전화번호를 조회
# 여기에서 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력, 전화번호 => - - - 하이픈 문자열을 삽입해서 출력
# ID 기준으로 내림차순(DESC)

# 일단 서로의 테이블에서 WRITER_ID와 USER_ID가 사용자의 ID이다. 이걸로 Inner JOIN 해야하며,
# 문제에서 게시물이 3건 이상 등록이라 하였으니, 게시물 데이터가 있는 USED_GOODS_BOARD를 기준으로 정보를 가져와야한다.
SELECT USER_ID, NICKNAME, CONCAT(CITY, ' ', STREET_ADDRESS1,' ', STREET_ADDRESS2) as 전체주소,
 CONCAT(SUBSTRING(TLNO, 1, 3), '-', SUBSTRING(TLNO, 4, 4), '-', SUBSTRING(TLNO, 8, 4)) as 전화번호
FROM USED_GOODS_USER USER
JOIN (
    SELECT WRITER_ID
    FROM USED_GOODS_BOARD
    GROUP BY WRITER_ID
    HAVING COUNT(WRITER_ID) >= 3
) BOARD ON USER.USER_ID = BOARD.WRITER_ID
ORDER BY USER_ID DESC
# FORMAT은 MYSQL 또는 일부 DBMS에서 지원하지 않을 수 있음.
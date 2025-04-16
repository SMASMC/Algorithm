# 20 : 58

# ANIMAL_OUTS테이블의 ANIMAL_ID는 ANIMAL_INS의 외래키
# 보호소에서 나갈 당시에 중성화 된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회 SQL
# 일단 동물들의 ANIMAL_ID로 서로의 테이블을 union 혹은 inner join을 쓰고,
# SEX_UPON이 다르게 된 데이터만 걸러서 출력해보자
# 서브쿼리말고, join을 써볼까?

select ins.ANIMAL_ID, ins.animal_type, ins.name
from ANIMAL_INS as ins join ANIMAL_OUTS as outs
on ins.ANIMAL_ID = outs.ANIMAL_ID and ins.SEX_UPON_INTAKE != outs.SEX_UPON_OUTCOME

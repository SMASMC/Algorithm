# 2번 형질이 보유하지 않으면서 1번이나 3번 형질을 보유하고 있는 대장균 개체의 수
# 2번은 2, 1번은 1, 3번은 4
select count(id) as count
from ECOLI_DATA
where (GENOTYPE & 2) = 0 and ((GENOTYPE & 1) = 1 or (GENOTYPE & 4) =4)
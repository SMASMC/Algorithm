# 21 : 11
# 아이템의 희귀도가 RARE인 아이템들의 모든 다음 업그레이드(계층 구조) 아이템의 정보를 출력
# 결과는 아이템 ID를 기준으로 내림차순 정렬

select info.item_id as item_id, info.item_name as item_name, info.RARITY as RARITY
from item_tree as tree 
# 자식 아이템의 정보와 tree와 맞는지 확인
join item_info as info on tree.item_id = info.item_id
# 부모 아이템 정보가 tree에 있는지 확인
join item_info as info2 on tree.parent_item_id = info2.item_id
where info2.rarity = 'RARE'
order by item_id desc
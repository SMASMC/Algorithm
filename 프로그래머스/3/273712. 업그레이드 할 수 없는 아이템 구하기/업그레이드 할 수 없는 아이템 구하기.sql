# 14 : 16

# 각 아이템들은 오직 하나의 parent 아이템 id를 가지고,
# root 아이템의 parent 아이템 id는 null이다.

# parents_item_id가 없는 것을 찾아서 최종 출력
select info.item_id, info.item_name, info.rarity
from item_info as info join
item_tree as tree
on info.item_id = tree.item_id
where info.item_id not in (select PARENT_ITEM_ID from item_tree where parent_item_id is not null)
order by info.item_id desc
# 20 : 42
select item_id, item_name, rarity
from item_info
where item_id in (select tree.item_id from item_info info,item_tree tree 
                  where info.item_id = tree.parent_item_id 
                  and info.rarity = 'rare')
order by item_id desc
# parent_item_id를 따라 찾아서 올라간 다음에 최상위(root)에 도달하면, 그만 찾는 것으로 해야함
# tree같은 느낌으로 찾아 올라가야함.
# 14 : 05

# from에서 table에 null인 것을 찾아서 넣는 것으로 해보자
select item_id, item_name
# from (
#     select item_id, item_name
#     from 
# )
from item_info
where ITEM_ID IN (
    select item_id
    from item_tree
    where PARENT_ITEM_ID is NULL
)
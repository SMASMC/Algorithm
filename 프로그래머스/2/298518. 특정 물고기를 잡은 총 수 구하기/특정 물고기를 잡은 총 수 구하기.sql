select count(info.id) as fish_count
from fish_info as info inner join fish_name_info as name_info
on info.fish_type = name_info.fish_type
where name_info.fish_name = 'BASS' or  name_info.fish_name = 'SNAPPER'

select id, email, first_name, last_name
from DEVELOPERS
where
skill_code & (select code from skillcodes where name='Python')
or
skill_code & (select code from skillcodes where name='C#')
order by id asc
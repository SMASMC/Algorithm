T = int(input())

result_list = []

for t in range(T):
    vps_list = list(input())
    vps_str = []
    for vps in vps_list:
        if vps == "(":
            vps_str.append(vps)
        elif vps == ")":
            if not vps_str:
                result_list.append("NO")
                break
            else:
                vps_str.pop()
    else: # for문이 break 없이 끝까지 수행됐을 경우에만 실행된다.
        if not vps_str:
            result_list.append('YES')
        else:
            result_list.append('NO')
for result in result_list:
    print(result)
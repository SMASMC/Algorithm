# 1620 나는야 포켓몬 마스터 이다솜
# 16 : 12

N , M = map(int, input().split()) # N : 포켓몬의 수 M : 맞춰야하는 문제의 수


# 포켓몬의 이름은 모두 영어로만 이루어져있고, 또, 음... 첫 글자만 대문자이고, 
# 나머지 문자는 소문자로만 이루어져 있어. 아참! 일부 포켓몬은 마지막 문자만 대문자
# 알파벳으로만 들어오면 포켓몬 번호를 말해
# 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력

# 총 N의 문제를 입력한 뒤, M의 문제가 쥐어진다.
# 그 뒤, 해당되는 문자 또는 값을 출력하면 된다.
# dictionary를 넣자
pokemon_list = []
pokemon_dict = {}
answer_list = []

for n in range(N):
    pokemon = input()
    pokemon_list.append(pokemon) # 포켓몬 위치
    pokemon_dict[pokemon] = n # 포켓몬 이름에 따른 위치 정보

for m in range(M):
    answer = input()
    if answer.isdigit(): # 숫자인 경우
        # 위치는 0부터 조회해야 함으로
        # -1을 해야 찾음
        find_pokemon = pokemon_list[int(answer) - 1]
        answer_list.append(find_pokemon)
    else: # 포켓몬 이름을 입력했을 경우
        answer_list.append(pokemon_dict[answer] + 1) # value가 들어감
for m in range(M):
    print(answer_list[m])
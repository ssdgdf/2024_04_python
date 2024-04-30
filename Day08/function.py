# 함수
# 마술상자 : [100->500 , 200->1000, 300->x]
# f(x) => len(x),str(x),int(x),print(x),input(x)
# count("p")

def koreaIT(x):
    return x + "코리아아이티"
a = koreaIT("인천점 ")
print(a)

def add(x, y):
    return x + y
a = add(1, 5)
print(a)

# 어떠한 단어를 넣었을 때 그 단어가 6글자 이상이면 글자가 길어요 아니면 글자가 짧아요
def word(x):
    if len(x)>=5:
        return "글자가 길어요"
    else:
        return "글자가 짧아요"

# 함수 : input ->[로직]->output

# abc(3,'🥟')
#['🥟','🥟','🥟']
def abc(x,y):
    return [y for x in range(x)]

#🥚🐣🐥🐓🍗
#🥚->🐣->🐥->🐓->🍗
def eggs(x):
    if x =='🥚':
        return '🐣'
    elif x == '🐣':
        return '🐥'
    elif x == '🐥':
        return '🐓'
    elif x == '🐓':
        return '🍗'
    else:
        return "에러"
print(eggs('🐓'))






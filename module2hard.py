import random
x = random.randint(3, 21)
list_key = str()
for i in range(1,21):
    if i != x and i < x:
        for j in range(1,21):
            if j != i and x % (i + j) == 0:
                list_key += str(i)+str(j)
print('Ваш код', x)
print('Ваш пароль', list_key)



def key ():
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    random_element= random.choice(num)
    return random_element
n = key()

def result (n):
    dict_sipher = {3:12, 4:13, 5:1423, 6:121524, 7:162534, 8:13172635, 9:1218273645, 10:141923283746,
                   11:11029384756, 12:12131511124210394857, 13:112211310495867, 14:1611325212343114105968,
                   15:1214114232133124115106978, 16:1317115262143531341251161079, 17:11621531441351261171089,
                   18:12151811724272163631545414513612711810, 19:118217316415514613712811910,
                   20:13141911923282183731746416515614713812911}
    dict_sipher_1 = dict_sipher.get(n)
    return dict_sipher_1

n = key()
print('Ваш код из словаря: ', n, ')')
dict_sipher_1 = result(n)
for i in range(3,21):
    if n == i:
      print('Ваш пароль из словаря: ', dict_sipher_1,')')
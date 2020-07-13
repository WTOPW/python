#-*— coding:utf-8 -*-
#Auther: wangjiana
Game_display = """
--------------------------------------<welcome {a} to this games>----------------------------------------------------
Choose your role :
    1、唐  僧 
    2、白骨精
""".format(a = "Game player")
print(Game_display)
Choose_role = input("choose your role 1 or 2 :")
print('-'* 125)
if Choose_role == "1" :
    print("you  choose role is [唐僧]")
elif Choose_role == "2" :
    print("You've chosen bone white to be shameless ,Assign [唐僧] of by default")
else :
    print("Wrong input, default assignment [唐僧]")

palyer_life = 10
palyer_attack = 10

boss_life = 20
boss_attack = 10
print('-'* 125)
print(f'the palyer_life of [唐僧]  is {palyer_life}, the palyer_attack of [唐僧] is {palyer_attack}')
while True :
    paly_game = """
    --------------------------------------<welcome {a} to this games>----------------------------------------------------
    Choose your role :
        1、练级 
        2、打boss
        3、逃跑
    """.format(a = "Game player")
    print(paly_game)
    Choose_game = input("choose your role 1 or 2 or 3:")
    if Choose_game == "1" :
        palyer_life += 2
        palyer_attack +=2
        print(f'the palyer_life of [唐僧]  is {palyer_life}, the palyer_attack of [唐僧] is {palyer_attack}')
    elif Choose_game == "2" :
        boss_life -= palyer_attack
        print('-' * 125)
        print('唐僧攻击了白骨精')
        if boss_life <= 0 :
            print(f'this boss is dead Game player  win')
            break
        palyer_life -= boss_attack
        print('白骨精攻击了唐僧')
        if palyer_life <= 0 :
            print(f'this palyer is dead Game player  win')
            break
    elif Choose_game == "3" :
        break
    else:
        print("重新输入")










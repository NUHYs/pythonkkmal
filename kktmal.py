import re
import random
import time

BRIGHT_RED1 = '\033[91m'
BRIGHT_ORAN = '\033[38;5;208m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_GREEN = '\033[32m'
BRIGHT_LGREEN = '\033[92m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_INDIGO = '\033[34m'
BRIGHT_PUPLE = '\033[35m'
BRIGHT_END = '\033[0m'

oneclearbool = False
chemicalbool = False
okokbool = False
oneclearbool2 = True
chemicalbool2 = True
okokbool2 = True

okoki = input(' 어인정을 키시겠습니까?(게임중에 종료 불가능) \"ㅇㅇ\", \"ㄴㄴ\" 를입력해주세요.')
while okokbool2:
    if okoki == "ㅇㅇ" or okoki == "dd":
        okokbool = True
        print(" 어인정이 켜졌습니다.")
        okokbool2 = False
        break
    elif okoki == "ㄴㄴ" or okoki == "ss":
        okokbool = False
        print(" 어인정이 꺼졌습니다.")
        okokbool2 = False
        break
    else:
        print(" " + okoki + "은 \"ㅇㅇ\", \"ㄴㄴ\" 가 아닙니다. 제대로입력해주세요")
        okoki = input(' 어인정을 키시겠습니까?(게임중에 종료 불가능) \"ㅇㅇ\", \"ㄴㄴ\" 를입력해주세요.')
chemicali = input(' 화학단어를 키시겠습니까?(게임중에 종료 불가능) \"ㅇㅇ\", \"ㄴㄴ\" 를입력해주세요.')
while chemicalbool2:
    if chemicali == "ㅇㅇ" or chemicali == "dd":
        chemicalbool = True
        print(" 화학단어가 켜졌습니다.")
        chemicalbool2 = False
        break
    elif chemicali == "ㄴㄴ" or chemicali == "ss":
        okokbool = False
        print(" 화학단어가 꺼졌습니다.")
        chemicalbool2 = False
        break
    else:
        print(" " + chemicali + "은 \"ㅇㅇ\", \"ㄴㄴ\" 가 아닙니다. 제대로입력해주세요")
        chemicali = input(
            ' 화학단어를 키시겠습니까?(게임중에 종료 불가능) \"ㅇㅇ\", \"ㄴㄴ\" 를입력해주세요.')
onecleari = input(' 한방단어를 키시겠습니까?(게임중에 종료 불가능) \"ㅇㅇ\", \"ㄴㄴ\" 를입력해주세요.')
while oneclearbool2:
    if onecleari == "ㅇㅇ" or onecleari == "dd":
        oneclearbool = True
        print(" 한방단어가 켜졌습니다.")
        oneclearbool2 = False
        break
    elif onecleari == "ㄴㄴ" or onecleari == "ss":
        oneclearbool = False
        print(" 한방단어가 꺼졌습니다.")
        oneclearbool2 = False
        break
    else:
        print(" " + onecleari + "은 \"ㅇㅇ\", \"ㄴㄴ\" 가 아닙니다. 제대로입력해주세요")
        onecleari = input(
            ' 한방단어를 키시겠습니까?(게임중에 종료 불가능) \"ㅇㅇ\", \"ㄴㄴ\" 를입력해주세요.')


with open('dict.txt', 'rt', encoding='utf-8') as f:
    af = f.read()

if okokbool == True:
    with open('lightnovel.txt', 'rt', encoding='utf-8') as f:
        df = f.read()
    with open('star.txt', 'rt', encoding='utf-8') as f:
        ef = f.read()
    with open('animation.txt', 'rt', encoding='utf-8') as f:
        bf = f.read()
else:
    pass

if chemicalbool == True:
    with open('chemical.txt', 'rt', encoding='utf-8') as f:
        cf = f.read()
else:
    pass


pat = re.compile('^[ㄱ-ㅎ가-힣]+$')
wordDict = dict()
hanbangSet = set()

# 한글로만 이루어져있고, 길이가 2 이상인 단어만 추출
for i in sorted([i for i in af.split() if pat.match(i) and len(i) >= 2], key=lambda x: -len(x)):
    if i[0] not in wordDict:
        wordDict[i[0]] = set()
    wordDict[i[0]].add(i)

if okokbool == True:
    for i in sorted([i for i in bf.split() if pat.match(i) and len(i) >= 2], key=lambda x: -len(x)):
        if i[0] not in wordDict:
            wordDict[i[0]] = set()
        wordDict[i[0]].add(i)

    for i in sorted([i for i in df.split() if pat.match(i) and len(i) >= 2], key=lambda x: -len(x)):
        if i[0] not in wordDict:
            wordDict[i[0]] = set()
        wordDict[i[0]].add(i)

    for i in sorted([i for i in ef.split() if pat.match(i) and len(i) >= 2], key=lambda x: -len(x)):
        if i[0] not in wordDict:
            wordDict[i[0]] = set()
        wordDict[i[0]].add(i)
else:
    pass

if chemicalbool == True:
    for i in sorted([i for i in cf.split() if pat.match(i) and len(i) >= 2], key=lambda x: -len(x)):
        if i[0] not in wordDict:
            wordDict[i[0]] = set()
        wordDict[i[0]].add(i)
else:
    pass

# 한방단어 제거 & 추출
if oneclearbool == True:
    for i in wordDict:
        delList = list()
        for j in wordDict[i]:
            if j[-1] not in wordDict:
                delList.append(j)
        for j in delList:
            hanbangSet.add(j)
            wordDict[i].remove(j)
else:
    pass

print(BRIGHT_RED1 + ' [중요] Ctrl+Z를 입력하면 기권할 수 있습니다.' + BRIGHT_END)

okokstr = ""
chemicalstr = ""
oneclearstr = ""

if okokbool == True:
    okokstr = "어인정, "
if chemicalbool == True:
    chemicalstr = "화학단어, "
if oneclearbool == True:
    oneclearstr = "한방단어"

print(BRIGHT_BLUE + ' [세팅] 게임세팅: ' + okokstr +
      chemicalstr + oneclearstr + '가 켜져있습니다.' + BRIGHT_END)
print(BRIGHT_RED1 +
      ' [중요] 게임도중 "게임 그만두기", "게임종료", X 표시를 눌르면 게임이 종료됩니다.' + BRIGHT_END)
round, win, lose = 0, 0, 0

while True:
    fallbool = True
    fallsint = 0
    winbool = False
    falls = input(' 몇번이상 틀리면 아웃으로 할지 정해주세요(숫자만 가능1 ~ 20)')
    while fallbool:
        if falls == str(falls):
            if (falls == '1' or falls == '2' or falls == '3' or falls == '4' or falls == '5' or falls == '6' or falls == '7' or falls == '8' or falls == '9' or falls == '10' or falls == '11' or falls == '12' or falls == '13' or falls == '14' or falls == '15' or falls == '16' or falls == '17' or falls == '18' or falls == '19' or falls == '20'):
                print(" 당신은 " + str(falls) + "번 틀리면 아웃입니다")
                fallbool = False
                break
            elif falls == "NUHY":
                print(BRIGHT_RED1 + " 당신은 틀려도 아웃되지 않습니다." + BRIGHT_END)
                fallbool = False
                winbool = True
                break
            else:
                fallsint + 1
                if fallsint == 5:
                    print(" 좀쓰라고.....;;;;")
                elif fallsint == 10:
                    print(" 너병있냐????")
                elif fallsint >= 15:
                    print(" 제발써주세요ㅠㅠㅠㅠㅠ...")
                print(' \"' + str(falls) + '\" 말고 숫자만 써주세요')
                falls = input(' 몇번이상 틀리면 아웃으로 할지 정해주세요(숫자만 가능)')
        else:
            print(' \"' + str(falls) + '\" 말고 문자를 써주세요')
            falls = input(' 몇번이상 틀리면 아웃으로 할지 정해주세요(숫자만 가능)')
    # 라운드 시작
    round += 1
    fall = 0
    print("\n" + "-" * 50)
    print("\n %d라운드를 시작합니다. 현재 %d승 %d패" % (round, win, lose))
    lastWord = ''
    alreadySet = set()
    firstTurn = True
    resetRound = False

    while True:
        # CPU 턴
        print()
        if firstTurn:
            lastWord = random.choice(
                list(wordDict[random.choice(list(wordDict.keys()))]))
            alreadySet.add(lastWord)
            print(' 컴퓨터 : ' + lastWord)
            firstTurn = False
        else:
            firstLetter = lastWord[-1]
            if not list(filter(lambda x: x not in alreadySet, wordDict.get(firstLetter, set()))):
                # 라운드 종료
                print(BRIGHT_LGREEN + ' 컴퓨터 : ^Z' + BRIGHT_END)
                print(BRIGHT_ORAN +
                      '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                print(BRIGHT_ORAN +
                      '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                print(BRIGHT_ORAN +
                      '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                print(BRIGHT_ORAN +
                      '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                print(BRIGHT_ORAN +
                      '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                print(BRIGHT_ORAN +
                      '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                print(BRIGHT_ORAN +
                      '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                win += 1
                break
            else:
                nextWords = sorted(filter(lambda x: x not in alreadySet,
                                          wordDict[firstLetter]), key=lambda x: -len(x))[:random.randint(20, 50)]
                lastWord = nextWords[random.randint(
                    0, random.randrange(0, len(nextWords)))]
                alreadySet.add(lastWord)
                print(' 컴퓨터 : ' + lastWord)

        # 유저 턴
        while True:
            # n번이상 틀렸을떄
            if winbool == True:
                pass
            else:
                if fall == int(falls):
                    print(' [결과] 당신은 ' + falls + '번이상 틀렸습니다')
                    fall = 0
                    resetRound = True
                    lose += 1
                    break
            print()
            try:
                yourWord = input(' YOU : ')
            except:
                print('\n [결과] 당신은 기권했습니다. CPU의 승리입니다!')
                print(' [힌트] ', end='')
                print(', '.join(list(filter(lambda x: x not in alreadySet,
                      wordDict.get(lastWord[-1], set())))[:3]))
                resetRound = True
                lose += 1
                break
            firstLetter = yourWord[0]
            if firstLetter != lastWord[-1]:
                if yourWord == "바탕빨":
                    print(BRIGHT_RED1)
                elif yourWord == "바탕주":
                    print(BRIGHT_ORAN)
                elif yourWord == "바탕노":
                    print(BRIGHT_YELLOW)
                elif yourWord == "바탕초":
                    print(BRIGHT_GREEN)
                elif yourWord == "바탕파":
                    print(BRIGHT_BLUE)
                elif yourWord == "바탕남":
                    print(BRIGHT_INDIGO)
                elif yourWord == "바탕보":
                    print(BRIGHT_PUPLE)
                elif yourWord == "바탕돌리기":
                    print(BRIGHT_END)
                elif yourWord == "게임 그만두기" or yourWord == "게임종료":
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    time.sleep(1)
                    quit()
                elif yourWord == "NUHY":
                    print(BRIGHT_LGREEN + ' 컴퓨터 : ^Z')
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    win += 1
                    resetRound = True
                    break
                print(" [오류] '" + lastWord[-1] + "' (으)로 시작하는 단어를 입력하세요.")
            elif yourWord in hanbangSet:
                if yourWord == "바탕빨":
                    print(BRIGHT_RED1)
                elif yourWord == "바탕주":
                    print(BRIGHT_ORAN)
                elif yourWord == "바탕노":
                    print(BRIGHT_YELLOW)
                elif yourWord == "바탕초":
                    print(BRIGHT_GREEN)
                elif yourWord == "바탕파":
                    print(BRIGHT_BLUE)
                elif yourWord == "바탕남":
                    print(BRIGHT_INDIGO)
                elif yourWord == "바탕보":
                    print(BRIGHT_PUPLE)
                elif yourWord == "바탕돌리기":
                    print(BRIGHT_END)
                elif yourWord == "게임 그만두기" or yourWord == "게임종료":
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    time.sleep(1)
                    quit()
                elif yourWord == "NUHY":
                    print(BRIGHT_LGREEN + ' 컴퓨터 : ^Z')
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    win += 1
                    resetRound = True
                    break
                if oneclearbool == True:
                    print(BRIGHT_LGREEN + ' 컴퓨터 : ^Z')
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    win += 1
                    resetRound = True
                    break
                else:
                    print(' [오류] 한방단어는 사용할 수 없습니다.')
            elif yourWord in alreadySet:
                if yourWord == "바탕빨":
                    print(BRIGHT_RED1)
                elif yourWord == "바탕주":
                    print(BRIGHT_ORAN)
                elif yourWord == "바탕노":
                    print(BRIGHT_YELLOW)
                elif yourWord == "바탕초":
                    print(BRIGHT_GREEN)
                elif yourWord == "바탕파":
                    print(BRIGHT_BLUE)
                elif yourWord == "바탕남":
                    print(BRIGHT_INDIGO)
                elif yourWord == "바탕보":
                    print(BRIGHT_PUPLE)
                elif yourWord == "바탕돌리기":
                    print(BRIGHT_END)
                elif yourWord == "게임 그만두기" or yourWord == "게임종료":
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    time.sleep(1)
                    quit()
                elif yourWord == "NUHY":
                    print(BRIGHT_LGREEN + ' 컴퓨터 : ^Z')
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    win += 1
                    resetRound = True
                    break
                print(' [오류] 이미 나온 단어입니다.')
            elif yourWord not in wordDict.get(firstLetter, set()):
                fall = fall + 1
                if yourWord == "바탕빨":
                    print(BRIGHT_RED1)
                    fall = 0
                elif yourWord == "바탕주":
                    print(BRIGHT_ORAN)
                    fall = 0
                elif yourWord == "바탕노":
                    print(BRIGHT_YELLOW)
                    fall = 0
                elif yourWord == "바탕초":
                    print(BRIGHT_GREEN)
                    fall = 0
                elif yourWord == "바탕파":
                    print(BRIGHT_BLUE)
                    fall = 0
                elif yourWord == "바탕남":
                    print(BRIGHT_INDIGO)
                    fall = 0
                elif yourWord == "바탕보":
                    print(BRIGHT_PUPLE)
                    fall = 0
                elif yourWord == "바탕돌리기" or yourWord == "배경돌리기" or yourWord == "배경되돌리기" or yourWord == "바탕되돌리기":
                    print(BRIGHT_END)
                    fall = 0
                elif yourWord == "게임 그만두기" or yourWord == "게임종료":
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    print(BRIGHT_RED1 + "게임이 종료됩니다." + BRIGHT_END)
                    time.sleep(1)
                    fall = 0
                    quit()
                elif yourWord == "NUHY":
                    print(BRIGHT_LGREEN + ' 컴퓨터 : ^Z')
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    print(BRIGHT_ORAN +
                          '\n [결과] 컴퓨터 기권했습니다. 당신의 승리입니다!' + BRIGHT_END)
                    win += 1
                    fall = 0
                    resetRound = True
                    break
                print(' [오류] 사전에 없는 단어입니다.')
                if winbool == True:
                    print(' [결과] 틀린횟수: @*#%!*&%#&(@&!#afsd#%$@#*@*번')
                else:
                    print(' [결과] 틀린횟수: ' + str(fall) + '번')
            else:
                alreadySet.add(yourWord)
                lastWord = yourWord
                break

        if resetRound:
            # 라운드 종료
            break

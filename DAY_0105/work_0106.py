'''
문자열 리스트를 입력 받아서 내림차순 결과 가장 낮은 문자열과 가장 높은 문자열을
 출력하는 함수를 구현하세요.
['Good', 'child', 'Zoo', 'apple', 'Flower', 'zero']
'''
# def min_max_str(words):
#     words.sort(reverse=True)
#     print(f"정렬 결과 : {words}")
#     print(f"가장 높은 문자열 : {words[0]}, 가장 낮은 문자열 : {words[-1]}")
# strList = input("msg=")[2:-2].split("', '")
# # print(strList)
# min_max_str(strList)
# a = ['Good', 'child', 'Zoo', 'apple', 'Flower', 'zero']

'''
2. 키보드로 입력 받은 데이터 중에서 숫자만 모두 저장하여 합계, 최대값, 최소값을
 출력하는 함수를 구현하세요.
하늘 Apple 2021 -9 False 23 7 None 끝
A 홍길동 False True True None Good Luck 가나다라
'''
# datas = input("데이터 입력 : ").split()
# numList = []
# for data in datas:
#     if not (data.isalpha()):
#         numList.append(data)
# numList = [int(num) for num in numList]
# if not(len(numList)):
#     numList.append(0)
# print(f"합계 : {sum(numList)} 최댓값 : {max(numList)} 최솟값 : {min(numList)}")

'''
3. 아래 조건을 만족하는 코드를 작성하세요.
- 'q', 'Q' 입력 전까지 동작
- 대문자 Q 제외한 나머지 알파벳 입력 시 ♠ 출력
- 소문자 q 제외한 나머지 알파벳 입력 시 ♤ 출력
- 0 ~ 9 숫자 입력 시 숫자만큼의 ◎ 출력
'''
# while True:
#     inputAlpha = input("알파벳 입력 : ")
#     if inputAlpha in ["q", "Q"]:
#         break
#     if inputAlpha.isupper():
#         print("♠")
#     elif inputAlpha.islower():
#         print("♤")
#     elif inputAlpha.isdigit():
#         print("◎" * int(inputAlpha))
#     else:
#         print("잘못된 입력")

'''
4. 아래 조건을 만족하는 코드를 작성하세요.
- 수의 범위 : 1 ~ 100
- 3의 배수 숫자 
- 7의 배수 숫자
- 8의 배수 숫자
- 3, 7, 8의 배수 숫자로 구성된 숫자만 출력
- 단!! 중복된 숫자는 제거 하세요
'''
# numList = list(range(1, 101))
# result = []
# for num in [3, 7, 8]:
#     for i in range(num-1, 101, num):
#         result.append(numList[i])
# print(set(result))

'''
5. 문자열을 입력하면 코드값을 아래와 같이 출력해주는 함수를 구현해 주세요.
"가나다"
'''
# def encoding(strData):
#     result2 = ""
#     result10 =""
#     for d in strData[1:-1]:
#         result2+=bin(ord(d))
#         result10+=hex(ord(d))
#     print(f"{strData}의 인코딩 : {result10}")
#     print(f"{strData}의 인코딩 : {result2}")
# data = input("data=")
# encoding(data)

'''
6. 문자열 리스트와 정수 1개를 입력하면 아래와 같이 출력하는 함수를 구현해 주세요.
['askde', 'beach', 'surf'] n=2
['home','pitch','python'] n=1
'''
# def sortWord(datas):
#     n = int(datas[-1])
#     words = []
#     temp = ""
#     for i in datas:
#         if i.isalpha():
#             temp += i
#         else:
#             words.append(temp)
#             temp = ""
#     result = [] # 입력에서 단어만 뽑아낸 리스트
#     for idx, w in enumerate(words):
#         if len(w) > n:
#             result.append(words[idx])
#     print("n번째로 정렬 안한 상태", result)
#
#     words_dict = {} # key = n번째 요소 / value = 해당 단어
#     for word in result:
#         words_dict[word[n]] = word
#     # print(words_dict)
#     nList = sorted(list(words_dict.keys())) # n번째 알파벳들끼리 정렬
#     # print(nList)
#
#     result2 = []
#     for nAlpha in nList:
#         result2.append(words_dict[nAlpha])
#     print(result2)
#
# datas = input("datas : ")
# sortWord(datas)

'''
7. 아래와 같이 출력되는 함수를 구현해 주세요.
- 정수 리스트 안에 2가 포함된 연속된 부분 리스트를 찾아서 반환
- 정수 리스트 안에 2가 1개 포함 된 경우 [2] 반환
- 정수 리스트에 2가 없는 경우 [-1] 
 [ 0, 1, 2, 4, 5, 2, 9 ]
 [ 0, 1, 2, 4, 5, 2, 9, 3, 2, 8, 1 ]
 [ 0, 1, 2, 4, 5, 3, 1, 7 ]
 [ 0, 0, 0 ]
'''
# def cnt2(List):
#     numList = [int(i) for i in nums if i.isdigit()]
#     cnt = numList.count(2)
#     if cnt == 0:
#         return [-1]
#     elif cnt == 1:
#         return [2]
#     else:
#         idx1 = numList.index(2)
#         idx2 = idx1
#         for i in range(numList.count(2)-1):
#             idx2 = numList.index(2, idx2+1)
#         return numList[idx1:idx2+1]
#
# nums = input("nums : ")
# print(cnt2(nums))

'''
8. 아래와 같이 출력된 함수를 구현해 주세요.
[ -2, 3, 0, 2, -5 ]
ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
'''
# def sumZero(nums):
#     pass
#
# sum_list = [] # 모든 조합을 담은 리스트
# inData = list(map(int,input("nums : ")[1:-1].split(",")))
# sumZero(inData)

'''
9. 아래와 같이 출력된 함수를 구현해 주세요.
- 리스트 컨프리헨션으로 구현
'''
# def listConprehension(n):
#     mulList = [f"{n} * {i} = {n*i:>2}" for i in range(1, 10)]
#     print(mulList)
#     dan = " "+str(n)+"단"+" "
#     print(f"{dan:-^42}")
#     for idx, i in enumerate(mulList, 1):
#             print(i, end="\n" if idx%3 == 0 else "\t\t")
# num = int(input("단 : "))
# listConprehension(num)

'''
10. 숫자와 콤마로만 이루어진 문자열 data가 주어지면 이때, data에 포함되어있는 자연
 수의 합과 가장 작은 수, 가장 큰 수를 출력하는 함수를 구현하세요.
'123,42,98,18'
'1,234'
'''
# def sumMinMax():
#     data = input("data=")
#     dataList = [int(i) for i in data if i.isdigit()]
#     #     cnt = numList.count(2)
#     print(f'"{data[1:-1]}"의 합 : {sum(dataList)}, 가장 큰 수 : {max(dataList)}, 가장 작은 수 : {min(dataList)}')
#
# sumMinMax()

'''
11. 업-다운 빙고 게임 기능의 함수를 구현하세요.
- 컴퓨터에서 1 ~ 100 범위에서 임의의 수 하나 선정
- 사용자 입력 숫자와 선정된 수가 동일하면 입력 받기 중단
- 사용자 입력 숫자가 선정 수보다 큰 수인지 작은 수인지 힌트 출력
'''
import random
# def upDown():
#     ans = random.randint(1,100)
#     print(ans)
#     while True:
#         user = int(input("빙고 넘버 : "))
#         if user == ans:
#             print("정답 - *~ 빙고 ~*")
#             break
#         elif user < ans:
#             print(f"힌트 - {user}보다 큰 수")
#         else:
#             print(f"힌트 - {user}보다 작은 수")
#
# upDown()

'''
12. 2, 4, 8 게임은 숫자의 끝 자리가 2, 4, 8로 끝나는 숫자의 경우 다른 문자로 출력하는
 게임으로 아래 조건을 만족하도록 구현하자.
 - 숫자를 int형 타입으로 input함수를 이용하여 입력받는다. 
 - 2, 4, 8 숫자가 있을 경우 #을 나타나게 한다. 
 - 입력받은 숫자가 1000일 경우 1부터 1000 까지에 해당하는 2, 4, 8을 
 #으로 출력한다. 
 - 한 줄에 20개씩 출력한다.
 '''
# num = int(input("게임 정수 입력 : "))
# for idx, val in enumerate(range(1, num+1), 1):
#     if str(val)[-1] in ("2", "4", "8"):
#         print("#", end="")
#     else:
#         print(val, end="")
#     if idx%20 == 0:
#         print()


'''
13.  월(Month)을 입력 받아 해당 월(Month)의 영어와 계절을 출력하는 코드를 작성하세요.
- 월(Month)에 해당하지 않는 숫자 입력 시 “잘못된 데이터입니다” 출력

'''
# monSeason = {"1" : "Jan Winter",
#              "2" : 'Fab Winter',
#              "3" : "Mar Spring",
#              "4" : "April Spring",
#              "5" : "May Spring",
#              "6" : "June Spring",
#              "7" : "July Summer",
#              "8" : "August Summer",
#              "9" : "September Summer",
#              "10" : "October Fall",
#              "11" : "November Fall",
#              "12" : "December Winter"}
# mon = input("좋아하는 월 입력 : ")
# print(monSeason[mon] if mon in monSeason.keys() else "존재하지 않는 월입니다.")


'''
14. 숫자와 화폐단위 입력 받아 세자리 마다 쉼표(,) 찍어서 출력하는 기능을 구현하세요.
- 입력은 함수에 넣지 않습니다.
- 세자리 마다 쉼표와 화폐 단위를 구성해서 출력하는 사용자 정의 함수 생성
1234567, $
907, ￦
'''
# def comma(moneyStr):
#     num = int(moneyStr.split(",")[0])
#     money = moneyStr[-1]
#     print(f"{num:,}{money}")
#
# comma(input("숫자 입력 : "))

'''
15. 입력받은 숫자 월(Month)에 대한 영어와 한국어 표기를 출력하는 함수를 구현하세요
'''



'''
16. 입력받은 정수 2개에 대한 공약수를 모두 출력하는 함수를 만들어 주세요.
-약수란?
특정한 수를 다른 수로 나누었을 때, 그 나머지가 0이되는 수
-공약수란?
두 수가 공통으로 갖고 있는 약수
'''
# set 교집합
def divisor(num1, num2):
    num1set = set()
    num2set = set()
    for i in range(1, num1+1):
        if not(num1 % i):
            num1set.add(i)
    for i in range(1, num2+1):
        if not(num2 % i):
            num2set.add(i)
    print(f"{num1}과 {num2}의 약수 : {sorted(num1set.intersection(num2set))}")
n1, n2 = map(int, input("약수 구하고 싶은 수 : ").split())
divisor(n1, n2)
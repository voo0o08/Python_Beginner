#-----------------------------------------------
# [ 요청 ] 키보드로 숫자를 입력 받아서 입력 받은 숫자 만큼 *을 화면에 출력해 주세요~
# 1) 숫자 입력 받기
# 2) 입력 받은 숫자 만큼 *출력하기
#-----------------------------------------------
num = input("정수 입력 : ")
if len(num)>0:
    num = int(num)
    print(num*"*")
else:
    #False일 때 실행
    print("입력된 숫자가 없습니다.")
print("end")



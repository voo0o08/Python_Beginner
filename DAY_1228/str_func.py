'''
str과 관련한 내장함수 알아보기
'''
msg = "Christmas2023!"

# 원소/요소의 개수를 알려주는 내장함수 => len()
# 사람문자 -> 기계어 : 인코딩
print(f'len(msg) => {len(msg)}개') # 숫자int, float 데이터 길이 개념x

# 해당하는 문자의 코드 값을 알려주는 내장 함수 => ord(문자1개)
print(ord('a'))

# H의 코드값 출력하기
code_h = ord("h")

# 코드값에 해당하는 문자를 반환해주는 내장 함수 => chr(아스키 코드 값)
# 기계어 -> 사람문자 : 디코딩
# 65에 해당하는 문자반환
print(f"chr(65) => {chr(65)}")
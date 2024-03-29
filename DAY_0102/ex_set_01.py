'''
set data type
- 목적 : 중복 데이터 제거
- 특징 : 이미 존재하는 데이터는 저장하지 않는다.
- 문법 : {데이터1, 데이터2, ... ,데이터n}
'''
aList=[]
aTuple = ()
aDict = {}
aSet = set()

# 생성자 함수 => 타입 이름과 동일한 함수명
# - 힙 영역에 메모리 공간 잡고 데이터 초기화 기능을 수행해줌
aList = list()
aTuple = tuple()
aDict = dict()
aSet = set()
# 7-10line처럼 기호만으로 가능한 경우도 있음

# ------------------------------------------------
# set 타입의 데이터 생성
# ------------------------------------------------
a1 = {1, 1, 2, 3, 4, 5, 1, 1, 1, 1}
print(a1)

# 다른 데이터 타입에서 중복 데이터 제거 시에 활용 => 형변환
a2 = [1, 1, 2, 3, 4, 5, 1, 1, 1, 1]
a2 = list(set(a2))
print(a2)

# 원소/요소 추가 => 1개 추가 : add()메서드
a1.add(10)
print(a1)

# 원소/요소 추가 => 여러개 추가 : update()메서드
a1.update([11, 22, 33, 44])
print(a1)

a1.add("good") # 한 덩어리로 들어감
print(a1)

a1.update("bad") # 조각조각 분리됨
print(a1)

# 원소 삭제 => remove(데이터) : return 없음
a1.remove("good")
print(a1)

# 원소/요소 꺼내기 => pop() : return 있음
data = a1.pop()
print(f"data = {data}, {a1}")

# 원소/요소 꺼내기 => discard(data)


# 집합에 관련된 메서드들과 기호/연산자
a1.clear()
a1.update("Happy")
# 교집합 & =====================================
# - 여러 개의 집합에 공통으로 존재하는 데이터만 추출
# - 메서드 : intersection()
a2 = a1.intersection({"a", "b", "A", "B"})
print(f"a2 = {a2}")

# 합집합 | =====================================
a2 = a1.union({"a", "b", "A", "B"})
print(f"a2 = {a2}")

# 차집합 - =====================================
# -기호/연산자 : -
# -메서드 : difference()
a3 = a1.union({"a", "b", "A", "B"})
print(f"a2-a1 = {a2-a1}")

# 정렬 ----------------------------------------
# => 원소 값을 서로 비교하여 정렬하는 것
# set타입에는 정렬 메서드가 없어 내장함수 sorted() 사용
sorted_a2 = sorted(a2)
print(sorted_a2)
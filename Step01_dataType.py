#한줄 주석입니다.

"""
여기는 여러줄 주석입니다.
가나다라
"""

print("Step01 시작")

#python의 여러가지 데이터 타입에 대해 알아보자

#int
num1 = 10
#float 
num2 = 10.1

#str
myName = '최상우'
yourName = 'kt'
ourName = """kt cloud infra"""

print(myName)
print(ourName)

# 순서가 중요한 여러 데이터 관리가 필요할 때
# 내가 좋아하는 음식 3가지를 하나의 변수에 담는 법
foods=["피자","햄버거","치킨"] #list type 인덱스로 관리

print(foods)

# 순서가 중요하지 않은 여러 데이터 관리가 필요할 때
# 회원 1명의 정보
num=1
name="최상우"
addr="노원"

mem1 = {"num":1, "name":"최상우", "addr":"노원"} #dict type 키캆으로 관리

print(mem1)

# 순서가 중요치 않은 ㄷ ㅔ이터를 하나의 묶음으로 관리(키값 없이)
mySet = {"빨간사탕", "초록사탕", "노란사탕"} #set type

print(mySet)

# 특정 code 블럭을 필요한 시점에 일괄 실행하고 싶다면?

def store(): # 함수 생성(들여쓰기 기준으로 블럭 지정)
    print("냉장고 문을 연다")
    print("물건을 저장한다")
    print("냉장고 문을 닫는다")

print("함수 밖") # 들여쓰기가 다르기 때문에 함수에 포함되지 않음

store() # 함수 실행
returnValue = store() #함수는 실행한 후 값(리턴 값)을 반환한다. 반환되는 값이 없으면 None을 반환
print(returnValue)

# 어떤 변수를 빈 상태로 만들고 값을 나중에 넣고 싶을 때 None을 넣으면 된다
a = None
a = "test"

# 참과 거짓을 나타내는 data type (Bool)
isMan = True
isWoman = False
isDifferent = True
isRun = False

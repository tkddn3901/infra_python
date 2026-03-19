# Step06_Tuple.py

'''
    -TUPLE
    1. list type과 유사
    2. 읽기 전용(수정, 삭제 불가)
    3. 기능이 적기 때문에 처리 속도가 빠르다

    만드는 방법
    (value1, value2, value3, ...)
'''
#"one", "two", "three" 3개의 str type 데이터를 tuple에 순서대로 담고
#그 객체의 참조 값을 tuple type tuple1이라는 변수에 담기
tuple1: tuple = ("one", "two", "three")
result1 = tuple1[0]
result2 = tuple1[1]
result3 = tuple1[2]

print(result1, result2, result3)

#readonly이기 때문에 수정 삭제 불가
#del tuple1[0]
#tuple1.remove(0)
#tuple1[0] = "xxx"

#방 1개짜리 tuple type을 만들 때는 주의
tuple2 = ("viper",)#value 뒤에 ,를 붙여야 함

#괄호 없는 튜플 생성
tuple3 = 10,20,30

#tuple에 저장된 값을 여러 변수에 나눠 담기
a, b, c = tuple3

#두 변수에 있는 값을 서로 바꾸려면
first = "girl"
second = "boy"
"""
기존 방식
tmp = first
first = second
second = tmp
"""
#튜플로 하는 방식
first, second = second, first

print("end")
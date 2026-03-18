# dict type에 대해 알아보자

'''
    - dict type
    1. key:value 형태로 데이터를 저장
    2. 순서가 없는 데이터
    3. key 값을 이용해서 저장된 값을 참조
'''

# 회원 1명의 데이터
mem1 = {"num":1, "name":"choi", "isMan":True}
info1 = [1, "choi", True] #값이 어떤 것을 나타내는지 알기 어려움
print(mem1["num"])
print(mem1["name"])
print(mem1["isMan"])

# dict 안의 내용을 변수에 담기
a = mem1["num"]
b = mem1["name"]
c = mem1["isMan"]

# dict 안의 내용을 수정
mem1["num"]=2
mem1["name"]="sw"
mem1["isMan"]=False
print(mem1)

# 특정 key 값으로 저장된 내용 삭제
del mem1["isMan"]
print(mem1)

# 모든 값 삭제
mem1.clear()
print(mem1) 
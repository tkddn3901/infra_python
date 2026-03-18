# list type에 대해 알아보자

'''
 - list type
 1. 순서가 있다.
 2. 여러 type의 데이터를 저장할 수 있다.
 3. 값 변경 가능
'''

# 대부분 한가지 data type을 담는다
nums = [10,20,30]
names = ["이제동", "바이퍼", "프레이"]

# 여러가지 data type을 섞어 담을 수 있다.
datas = [10, "가", True]

nums.append(40)
print(nums)

# len() builtin 함수를 이용해서 list의 길잉를 얻을 수 있다.
nums_len = len(nums)
print(nums_len)

# 인덱스에 의한 참조
name0 = names[0]
print(name0)

# 인덱스를 이용해서 삭제
del names[0]
print(names)

# 값에 의한 삭제
names.remove("프레이")
print(names)

# 마지막 index를 삭제하면서 값을 가져오기
nums.pop()
result = nums.pop()
print(nums)
print(result)
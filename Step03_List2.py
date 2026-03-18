# list type에 대해 알아보자

nums = [10,20,30,40,50]
names = ["kim", "park", "jo", "oh", "choi"]

# list에 들어 있는 데이터를 앞에서부터 순서대로 참조하면서 어떤 동작을 할 때
print(nums)
for item in nums:
    print(item)

for item in names:
    print("names를 순서대로 출력중...")
    print(item)


r1 = range(5)
r2 = range(10)

print(r1)
print(r2)

for item in range(5):
    print(item)

# result2에 들어갈 값을 예상 -> range(5)와 같다
result2 = range(len(names))

for i in range(len(names)):
    print("list의 index와 함께 출력")
    print(i, names[i])



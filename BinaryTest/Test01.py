# BinaryTest/test01.py

# python에서 2진수 다루기

# 2진수는 숫자를 만들 때 prefix로 0b
num1 = 0b1010

result = num1+5
print(result)

# 10진수를 2진수로 변환
num2 = 150
result2:str = bin(num2)
print(result2)
print(type(result2))

print("--------------")

line = "abcde12345"
print(line[5:10])

# 위의 result2 문자열에서 (0bxxxxx)에서 0b를 제거한 순수 2진수 형태의 문자열만 얻어내려면?
print(result2[2:])
# str type에 대해 알아보자

# 양쪽에 공백이 포함되거나 포함될 가능성이 있는 문자열의 공백을 제거
text = "    Cloud Infra    "
result = text.strip()
print(result)

# .으로 분리
myIp = "192.168.0.2"
result2 = myIp.split(".")
print(result2)

# .으로 다시 합치기
result3 = ".".join(result2)
print(result3)

# 특정 문자열 찾아서 대체
result4 = "hello mimi!".replace("mi", "ma")
print(result4)

# 대소문자로 변환
result5 = "python".upper()
result6 = "PYTHON".lower()
print(result5)
print(result6)

print("끝")
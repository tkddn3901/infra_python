# Step08_Input.py

# 콘솔창으로부터 문자열 입력 받기

input_msg = input("메시지 입력 : ")

print(f"입력한 메시지 : {input_msg}")

input_name: str = input("input name : ")
input_addr: str = input("input addr : ")

print(f"name : {input_name}, addr : {input_addr}")

# 문자열로 입력
input_age : str = input("input age : ")
# 숫자로 형변환
age : int = int(input_age) + 1

print(f"당신은 내년에 {age}살 입니다.")
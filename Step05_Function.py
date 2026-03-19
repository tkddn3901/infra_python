# Step05_Function.py

'''
    function type

    -특정 시점에 여러 줄의 code를 일괄 실행하고자 할 때 사용한다.
    -함수도 data이다. (변수에 담을 수 있다.)
    -함수 안에 저장된 code를 일괄 실행 하는 것은 함수를 call 한다고 한다.
    -함수는 저장된 code를 다 실행하고 함수를 call 했던 위치로 흐름이 넘어온다.
    -call 했던 위치로 돌아오면서 어떤 data를 반드시 반환한다.
'''

from types import NoneType


def test1():
    print("test1() called")

test1()
result1 = test1()

# 매개변수가 선언된 함수
# 매개변수에 대입할 값을 전달해야 호출할 수 있다.
# 매개변수의 이름은 마음대로 지을 수 있다.
def test2(arg):
    print("전달 받은 내용 :", arg)
    print(f"전달 받은 내용 : {arg}")

test2(None)
test2(10)
test2("kim")

def print_sum(num1:int, num2:int):
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}")

print_sum(10, 20)
print_sum("kim", "choi")

def print_info(name:str, addr:str):
    print(f"name : {name} and address : {addr}")

print_info("viper", "china")
print_info(addr="china", name="viper")

def get_sum(num1: int, num2: int):
    sum=num1+num2
    return sum

result2 = get_sum(10, 20)
print(result2)

print("end")
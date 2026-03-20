# Step11_Class2.py

class MyCar:

    def __init__(self, name:str):
       print("생성자가 호출됨")
       print(self)
       # 객체 고유의 저장소에 전달된 값을 저장한다.
       self.name = name

    def drive(self):
       print(f"{self.name} is driving~")

if __name__ == "__main__" :
    c1: MyCar = MyCar("volvo")
    c2: MyCar = MyCar("bmw")
    c1.drive()
    c2.drive()
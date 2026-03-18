# Step03_Example.py

'''
    회원 한명의 정보는 번호, 이름, 주소로 이루어져 있다.
    그리고 그러한 회원이 여러명 이다.
    여러명의 회원 목록을 하나의 묶음으로(하나의 data) 순서대로 관리하고 싶다면
    => list 안에 dict를 넣어서 관리
'''

# 3명의 회원정보를 각각 dict에 담은 다음 그 dict를 list에 담는 코드를 작성해서 쳇팅장에 보내라

mem1 = {"num":1 , "name":"kim" , "addr":"가"}
mem2 = {"num":2 , "name":"park" , "addr":"나"}
mem3 = {"num":3 , "name":"choi" , "addr":"다"}

members = [mem1, mem2, mem3]

a = members
b = members[0]
c = members[0]["num"]
d = members[0]["name"]
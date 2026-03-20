# Step13_Example.py

from jinja2 import Template


info:dict = {
    "num":1,
    "name":"viper",
    "body":{
        "weight":70,
        "height":180
    },
    "hobby":["lol", "ad", "english"]
}

'''
    위의 info 안에 들어 있는 데이터를 이용해서 아래와 같은 형식의 문자열을 출력해 보세요.

    번호 : 1
    이름 : viper
    키 : 180cm
    몸무게 : 70kg
    취미 : 
        - lol 
        - ad 
        - english
'''

my_template='''
    번호 : {{num}}
    이름 : {{name}}
    키 : {{body.height}}
    몸무게 : {{body.weight}}
    취미 : 
        - {{hobby[0]}}
        - {{hobby[1]}}
        - {{hobby[2]}}
'''

temp:Template = Template(my_template)
result: str = temp.render(info)

print(result)
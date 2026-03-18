#Step04_Str2.py

'''
    여러분의 이름과 주소 좋아하는 음식 2가지를 작성해서 쳇팅장에 올려보세요
'''
# json은 javascript 객체 표기법을 따르는 문서 형식
'''json 작성 방법
    {
        "key":value
                10      숫자
                10.1    숫자
                "str"   문자
                true    논리
                false   논리
                {}      오브젝트
                []      배열
                null    빈 값
    }
'''
# info는 str type이긴 하지만 특별한 형식(json)을 띄고 있다.
import json


info = '''{
    "name":"최상우",
    "addr":"서울",
    "foods":["갈비", "피자"]
}
'''
# result는 str(json)의 문자열이 python의 dict로 변경된 값을 가지고 있다
result = json.loads(info)
print(result["name"])
print(result["addr"])
print(result["foods"][0])
print(result["foods"][1])

# result2는 dict의 데이터를 json 문자열로 변환된 값을 가지고 있다
result2 = json.dumps(result)
print(result2)

print("끝")
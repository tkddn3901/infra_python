# Step13_Jinja2_List2.py

# 게시글 목록이 담긴 리스트
from jinja2 import Template


posts:list = [
    {"id":1, "writer":"writer1", "title":"title1"},
    {"id":2, "writer":"writer2", "title":"title2"},
    {"id":3, "writer":"writer3", "title":"title3"}
]

'''
    위의 posts에 담긴 데이터를 이용해서 아래와 같이 출력되도록 해보세요.
    글 목록입니다.
    - 글번호:1 작성자:witer1 제목:title1
    - 글번호:2 작성자:witer2 제목:title2
    - 글번호:3 작성자:witer3 제목:title3
'''

my_template='''
    글 목록입니다.
    {% for i in posts -%}
    - 글번호:{{ i.id }} 작성자:{{ i.writer }} 제목:{{ i.title }}
    {% endfor %}
'''

temp:Template = Template(my_template)
result: str = temp.render(posts=posts)

print(result)
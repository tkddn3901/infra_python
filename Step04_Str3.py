# yaml 형식의 문자열 다루기

# yaml 문자열을 다룰 때는 외부 모듈을 pip로 설치를 해서 import 해야한다.

import yaml

info = '''
name: 최상우
addr: 서울
foods:
  - 갈비
  - 피자
isMan: true
body:
  weight: 75
  height: 174
'''

# info에 들어있는 문자열을 dict type으로 바꾸고 내용 확인 후 다시 yaml로 변환

result =  yaml.safe_load(info)
print(result)

result2 = yaml.safe_dump(result)
print(result2)

print("끝")
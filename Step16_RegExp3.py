# Step16_RegExp3.py

import re

logs = [
    "[INFO] Server started successfully.",
    "[WARN] Memory usage is high.",
    "[ERROR] Database connection failed.",
    "[DEBUG] x = 10"
]

# logs에서 ERROR or WARN 로그만 찾아서 콘솔창에 출력하기

elog = []

for line in logs:
    # re.search는 문자열 전체에서 패턴이 있는지 확인합니다.
    # "WARN|ERROR"는 "WARN 또는 ERROR"라는 뜻입니다.
    if re.search(r"^\[(WARN|ERROR)\]", line):
        elog.append(line)

# 결과 출력
for line in elog:
    print(line)
# Step17_File.py

import os

if __name__ == "__main__" :
    # 현재 작업 폴더의 경로
    print(os.getcwd())
    # 파일 구분자(window = \, linux = /)
    print(os.sep)

    '''
        현재 memo.txt 파일은 C:\playground\python_basic\memo.txt의 경로에 존재
        해당 경로를 문자열로 만들어보기
    '''

    path:str = os.path.join(os.getcwd(), "memo.txt")

    print(path)

    with open(path, "r", encoding="utf-8") as f: # r : 일기전용
        # 파일에서 문자열 읽기
        result = f.read()
        print("---memo.txt 파일의 내용---")
        print(result)
# Step17_File3.py

import os

if __name__ == "__main__" :

    letter_path = os.path.join(os.getcwd(), "my_letter.txt")

    with open(letter_path, "r", encoding="utf-8") as f:
        # 문자열을 한줄씩 읽어서 콘솔에 출력
        print(f.readline())
        print(f.readline())
        print(f.readline())
        print(f.readline().strip()) # 공백이나 개행기호 없애고 싶으면 strip()까지 호출
        print(f.readline().strip())
        print(f.readline().strip())

    print("---반복문으로 처리---")

    with open(letter_path, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
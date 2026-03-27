# Step17_File2.py

import os

if __name__ == "__main__" :
    
    # 새로운 파일을 만들어서 문자열을 파일에 출력하기
    letter_path = os.path.join(os.getcwd(), "my_letter.txt")

    # 기존의 내용을 제거하고 덮어쓰기
    with open(letter_path, "w", encoding="utf-8") as f:
        f.write("to my friend\n")
        f.write("hello\n")
        f.write("bye\n")

    # 파일을 열어서 문자열 추가하기 append mode
    with open(letter_path, "a", encoding="utf-8") as f:
        f.write("brbrbrbrbr\n")
        f.write("brbrbrbrbr\n")
        f.write("brbrbrbrbr\n")

    print("my_letter.txt 파일 생성 및 쓰기 완료")
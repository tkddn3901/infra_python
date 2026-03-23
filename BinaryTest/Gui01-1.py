# Gui01.py

# ui Toolkit을 사용할 수 있는 interface 객체 import 하기
import tkinter as tk
from tkinter import messagebox

# root 창 생성
root = tk.Tk()

# 제목 설정
root.title("나의 App")

# 창의 크기
root.geometry("400x200")

# 레이블
label = tk.Label(root, text="안녕하세요! python GUI 입니다.")
label.pack(pady=20)

# 입력창
nums_entry = tk.Entry(root, font=("Areal", 12))
nums_entry.pack(pady=5)
nums_entry.focus() #포커스 추가

def clicked():
    print("버튼을 클릭했네요")
    # Entry(입력창)에 입력한 문자열 읽어오기
    contents = nums_entry.get()
    if not contents.isdigit():
        messagebox.showwarning("경고", "문자를 입력했습니다!")
    else:
        nums = int(nums_entry.get())

    if nums > 255:
        messagebox.showwarning("경고", "255보다 큰 수를 입력했습니다!")
    else:
        # label text 수정하기
        label2.config(text=f"입력한 숫자 : {(nums):08b}")

# 버튼
btn = tk.Button(root, text="전송", command=clicked, width=10, bg="lightgray")
btn.pack(pady=15)

label2 = tk.Label(root, text="결과...")
label2.pack(pady=20)

# 창이 닫힐 때까지 무한 대기
root.mainloop()
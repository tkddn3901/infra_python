# BinaryTest/gui02.py
import tkinter as tk
from tkinter import messagebox

def clicked():
    print("버튼을 클릭했네요?")
    input_value = entry.get().strip()
    
    if not input_value:
        return 

    try:
        num = int(input_value)
        # 0-255 사이가 아니면 경고 알림
        if not (0 <= num <=255):
            messagebox.showerror("에러", "0-255 사이의 숫자를 입력해주세요.")
            return
        binary_result = f"{num:08b}"
        # 아래 result_label이 존재해야 합니다.
        result_label.config(text=binary_result, fg="blue")
    except Exception as e:
        result_label.config(text="숫자만 입력 가능 합니다", fg="red")

if __name__ == "__main__" :
    root = tk.Tk()
    root.title("나의 App")
    root.geometry("400x300") # 버튼과 결과창을 위해 세로 길이를 조금 늘렸습니다.

    label = tk.Label(root, text="10 진수를 2진수로 변환")
    label.pack(pady=10)

    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    entry.focus() 

    # --- 추가 및 수정된 부분 ---
    
    # 1. 함수를 실행할 버튼이 필요합니다.
    btn = tk.Button(root, text="변환", command=clicked)
    btn.pack(pady=10)

    # 2. 결과를 표시할 레이블이 미리 생성되어 있어야 합니다.
    result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
    result_label.pack(pady=20)

    # --------------------------

    root.mainloop()
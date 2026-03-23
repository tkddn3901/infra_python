# BinaryTest/gui02.py
import tkinter as tk
from tkinter import messagebox

def clicked():
    print("버튼을 클릭했네요?")
    input_value = entry.get().strip()

    if not input_value:
        return 

    try:
        num = input_value
        num_set = set(num).issubset({"0", "1"})
        if not (num_set):
            messagebox.showerror("에러", "2진수가 아닙니다.")
            return
        if len(num) > 8:
            messagebox.showerror("에러", "8자리가 넘습니다.")
            return
        binary_result = int(num, 2)
        result_label.config(text=binary_result, fg="blue")
    except Exception as e:
        result_label.config(text="문제가 발생했습니다.", fg="red")

if __name__ == "__main__" :
    root = tk.Tk()
    root.title("나의 App")
    root.geometry("400x300") # 버튼과 결과창을 위해 세로 길이를 조금 늘렸습니다.

    label = tk.Label(root, text="2 진수를 10진수로 변환")
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
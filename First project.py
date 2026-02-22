import tkinter as tk  # استدعاء مكتبة Tkinter

# إنشاء نافذة
window = tk.Tk()
window.title("أول نافذة لي يا عثمان")
window.geometry("300x200")  # حجم النافذة

# دالة عند الضغط على الزر
def say_hello():
    label.config(text="مرحبا يا عثمان!")

# نص في النافذة
label = tk.Label(window, text="اضغط الزر!")
label.pack(pady=20)

# زر
button = tk.Button(window, text="اضغطني", command=say_hello)
button.pack(pady=10)

# تشغيل النافذة
window.mainloop()
import tkinter as tk
import datetime

# 计算倒计时
def countdown():
    now = datetime.datetime.now()
    gaokao_date = datetime.datetime(2025, 6, 7)  # 2025年高考日期
    remaining = gaokao_date - now
    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    time_str = f"距离2025年高考还有{days}天 {hours}小时 {minutes}分钟 {seconds}秒"
    label.config(text=time_str)
    root.after(1000, countdown)  # 每秒更新一次

# 创建GUI
root = tk.Tk()
root.title("2025年高考倒计时")
root.resizable(0, 0)  # 禁止窗口缩放

# 设置字体颜色为红色
label = tk.Label(root, text="", font=("Helvetica", 48), fg="red")
label.pack()

countdown()

# 运行GUI
root.mainloop()

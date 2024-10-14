import customtkinter as ctk
from tkcalendar import DateEntry

win = ctk.CTk()

win.geometry('600x900')
win.title('네이버 지식인 검색')
win.option_add('*Font','맑은고딕 20')

f1=ctk.CTkFrame(win,width=1500,height=100)
f1.pack(side=ctk.TOP)
f2=ctk.CTkFrame(win,width=1500,height=550)
f2.pack()
f3=ctk.CTkFrame(win,width=1600,height=100)
f3.pack(side=ctk.BOTTOM)

# 네이버 지식인 로고
# img = PhotoImage(f1, file='naver_kin_program\img\네이버 지식인 로고.png').subsample(1)
# lab_d = ctk.CTkLabel(f1, image=img)
# lab_d.pack()

# 검색창
lab1 = ctk.CTkLabel(f2, text='검색어')
lab1.grid(row=0,column=0)

ent1 = ctk.CTkEntry(f2)
ent1.grid(row=0,column=1)

# 시작날짜
lab2 = ctk.CTkLabel(f2, text='시작날짜')
lab2.grid(row=1,column=0)

s_cal = DateEntry(f2,dateformat=3,width=12, background='darkblue',
                    foreground='white', borderwidth=4)
s_cal.grid(row=2,column=0)

# 끝날짜
lab2 = ctk.CTkLabel(f2, text='끝날짜')
lab2.grid(row=1,column=1)

e_cal = DateEntry(f2, dateformat=3, width=12, background='darkblue',
                    foreground='white', borderwidth=4)
e_cal.grid(row=2,column=1)

# 페이지수
lab2 = ctk.CTkLabel(f2, text='페이지 수(1~100)')
lab2.grid(row=3,column=0)

ent2 = ctk.CTkEntry(f2)
ent2.grid(row=3,column=1)

btn = ctk.CTkButton(f2, text='검색')
btn.grid(row=4,column=0,columnspan=2)

win.mainloop()
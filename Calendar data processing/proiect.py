from tkinter import *
from PIL import ImageTk, Image
import re
import clips as cl
  
def Problema1(env, date1_d, date1_m, date1_y, date2_d, date2_m, date2_y, answer):
    env.clear()
    env.load("./problema1.clp")
    env.reset()
    ##Daca una dintre casete este goala
    ok = 0
    if date1_d.get() == "" or date1_m.get() == "" or date1_y.get() == "" or date2_d.get() == "" or date2_m.get() == "" or date2_y.get() == "":
        answer.config(text=' ')
        answer.config(text='Este o problema')
        ok = 1
    ##Daca ce sa introdus nu este numar si este pozitiv
    if (
            date1_d.get().isnumeric() == False or date1_m.get().isnumeric() == False or date1_y.get().isnumeric() == False or
            date2_d.get().isnumeric() == False or date2_m.get().isnumeric() == False or date2_y.get().isnumeric() == False):
        answer.config(text=' ')
        answer.config(text='Este o problema')
        ok = 1
    ##Daca datele sunt identice
    if ok == 0:
        if date1_d.get() == date2_d.get() and date1_m.get() == date2_m.get() and date1_y.get() == date2_y.get():
            answer.config(text=' ')
            answer.config(text='Date identice')
            ok = 1
    ##Adaugare de facturi si dupa rulare 
    if ok == 0:
        env.assert_string(
            '(date (day ' + date1_d.get() + ')(month ' + date1_m.get() + ')(year ' + date1_y.get() + ')(nr 1))')
        env.assert_string(
            '(date (day ' + date2_d.get() + ')(month ' + date2_m.get() + ')(year ' + date2_y.get() + ')(nr 2))')
        env.assert_string('(rezultat (rez 0)(nr 1))')
        env.assert_string('(rezultat (rez 0)(nr 2))')
        env.run()
        raspuns = list(env.facts())
        raspuns = raspuns[0]
        answer.config(text=' ')
        answer.config(text=str(raspuns).split()[1].strip('()'))


def Problema2(env, day, month, year, number):

    env.clear()
    env.load("./problema2.clp")

    try:
        if int(day.get()) > 31 or int(month.get()) > 12 or int(year.get()) > 99999999:
            error_message = Label(root, text="Not a date", font=('Arial', 10)).place(x=600 // 6 + x * 5,
                                                                                     y=800 // 3.4 + dist + 140)
            return
        fact = f"(deffacts init (date (day {int(day.get())})  (month {int(month.get())}) (year {int(year.get())}) (stopNumber {int(number.get())})) (lean 0))"

    except ValueError:
        print("Only numbers please")
        error_message = Label(root, text="Only numbers", font=('Arial', 10)).place(x=600 // 6 + x * 5, y=800 // 3.4 + dist + 140)
        return
    env.build(fact)
    env.reset()
    env.run()
    print("Fapte pentru problema2.clp:")
    cnt = 0
    for fact in env.facts():
        if cnt == 0:
            cnt += 1
            my_list = re.findall('\d+', str(fact))
        # print(fact)
    text = f"{my_list[0]} / {my_list[1]} / {my_list[2]}"
    print(text)
    Result = Label(root, text=text, font=('Arial', 10)).place(x=600//6 + x*5,y=800//3.4+dist+140)
    try:
        if int(day.get()) > 31 or int(month.get()) > 12 or int(year.get()) > 99999999:
            error_message = Label(root, text="Not a date", font=('Arial', 10)).place(x=600 // 6 + x * 5,
                                                                                     y=800 // 3.4 + dist + 140)
            return
        fact = f"(deffacts init (date (day {int(day.get())})  (month {int(month.get())}) (year {int(year.get())}) (stopNumber {int(number.get())})) (lean 0))"

    except ValueError:
        print("Only numbers please")
        error_message = Label(root, text="Only numbers", font=('Arial', 10)).place(x=600 // 6 + x * 5, y=800 // 3.4 + dist + 140)
        return
    env.build(fact)
    print("Fapte pentru problema2.clp:")
    cnt = 0
    for fact in env.facts():
        if cnt == 0:
            cnt += 1
            my_list = re.findall('\d+', str(fact))
def Problema3a(env,day,month,year):
    env.clear()
    env.load("./problema3a.clp")
    print("Fapte pentru problema3a.clp:")
    for fact in env.facts():
        print(fact)
    try:
        if int(day.get()) > 31 or int(month.get()) > 12 or int(year.get()) > 99999999:
            error_message = Label(root, text="Not a date", font=('Arial', 10)).place(x=1000//6+450 + x,y=800//2+dist+100)
            return
        if int(year.get()) <  1970:
            error_message = Label(root, text="Too early", font=('Arial', 10)).place(x=1000//6+450 + x,y=800//2+dist+100)
            return
        fact = f"(deffacts init  (datec (day {int(day.get())}) (month {int(month.get())}) (year {int(year.get())}) (startday 1) (startmonth 1) (startyear 1970) (run 1)))"
    except ValueError:
        print("Only numbers please")
        error_message = Label(root, text="Only numbers", font=('Arial', 10)).place(x=1000//6+450 + x,y=800//2+dist+100)
        return
    env.build(fact)
    env.reset()
    env.run()
    cnt = 0
    for fact in env.facts():
        if cnt == 0:
            cnt += 1
            my_list = re.findall('\d+', str(fact))
    text = f"{my_list[3]}"
    print(text)
    Result = Label(root, text=text, font=('Arial', 10)).place(x=1000//6+450 + x,y=800//2+dist+100)
def Problema3b(env, timestamp):
    env.clear()
    env.load("./problema3b.clp")
    print("Fapte pentru problema3b.clp:")
    for fact in env.facts():
        print(fact)
    try:
        if int(timestamp.get()) < 0:
            error_message = Label(root, text="positive values only", font=('Arial', 10)).place(x=1000//6+450 + x,y=900//2+dist+100)
            return
        fact = f"(deffacts init  (datec (timestamp {int(timestamp.get())}) (startday 1) (startmonth 1) (startyear 1970) (run 1)))"
    except ValueError:
        print("Only numbers please")
        error_message = Label(root, text="Only numbers", font=('Arial', 10)).place(x=1000//6+450 + x,y=900//2+dist+100)
        return
    env.build(fact)
    env.reset()
    env.run()
    cnt = 0
    for fact in env.facts():
        if cnt == 0:
            cnt += 1
            my_list = re.findall('\d+', str(fact))
    text = f"{my_list[1]} / {my_list[2]} / {my_list[3]}"
    print(text)
    Result = Label(root, text=text, font=('Arial', 10)).place(x=1000//6+450 + x,y=900//2+dist+100)
env = cl.Environment()
root = Tk()
root.geometry("800x800")
dist = 50
image = Image.open("./image-background.jpg").resize((800, 800))
background_image = ImageTk.PhotoImage(image)
label = Label(root, image=background_image)
label.place(x=0, y=0)
x = 50
title=Label(root,text='Date processing',font=('Arial',26)).place(x=600//2 - 30,y=0)
Q3=Label(root,text='Number of epochi from  a date',font=('Arial',16)).place(x=600//6,y=800//2+dist+50)
Q2=Label(root,text='The new date after n days',font=('Arial',16)).place(x=600//6,y=800//3.4+dist)
Q1=Label(root,text=' Difference between 2 dates',font=('Arial',16)).place(x=600//6,y=800//7.7)
x = 50
Q1_date1_day=Label(root,text="Day",font=('Arial',10)).place(x=600//6 + x,y=800//7.6+50)
Q1_date1_day_input=Entry(root,font=('Arial',10),width=10)
Q1_date1_day_input.place(x=600//6+50 + x,y=800//7.6+50)
Q1_date1_mounth=Label(root,text="Mouth",font=('Arial',10)).place(x=600//6+150 + x,y=800//7.6+50)
Q1_date1_month_input=Entry(root,font=('Arial',10),width=10)
Q1_date1_month_input.place(x=600//6+210 + x,y=800//7.6+50)
Q1_date1_year=Label(root,text="Year",font=('Arial',10)).place(x=600//6+300 + x,y=800//7.6+50)
Q1_date1_year_input=Entry(root,font=('Arial',10),width=10)
Q1_date1_year_input.place(x=600//6+350 + x,y=800//7.6+50)
Q1_date2_day=Label(root,text="Day",font=('Arial',10)).place(x=600//6 + x,y=800//7.6+115)
Q1_date2_day_input=Entry(root,font=('Arial',10),width=10)
Q1_date2_day_input.place(x=600//6+50 + x,y=800//7.6+115)
Q1_date2_mounth=Label(root,text="Mouth",font=('Arial',10)).place(x=600//6+150 + x,y=800//7.6+115)
Q1_date2_mounth_input=Entry(root,font=('Arial',10),width=10)
Q1_date2_mounth_input.place(x=600//6+210 + x,y=800//7.6+115)
Q1_date2_year=Label(root,text="Year",font=('Arial',10)).place(x=600//6+300 + x,y=800//7.6+115)
Q1_date2_year_input=Entry(root,font=('Arial',10),width=10)
Q1_date2_year_input.place(x=600//6+350 + x,y=800//7.6+115)
Q1_answer=Label(root,text=" ",font=('Arial',10))
Q1_answer.place(x=600//6+450+50 + x,y=800//7.6+80)
Q1_submit=Button(root,text="Result",command=lambda: Problema1(env,
                                                              Q1_date1_day_input,
                                                              Q1_date1_month_input,
                                                              Q1_date1_year_input,
                                                              Q1_date2_day_input,
                                                              Q1_date2_mounth_input,
                                                              Q1_date2_year_input,
                                                              Q1_answer)).place(x=600//6+450 + x,y=800//7.6+80)

Q2_date_day=Label(root,text='Day',font=('Arial',10)).place(x=600//6 + x,y=800//3.4+dist+75)
Q2_date_day_input=Entry(root,font=('Arial',10),width=10)
Q2_date_day_input.place(x=600//6+50 + x,y=800//3.4+dist+75)
Q2_date_month=Label(root,text='Mouth',font=('Arial',10)).place(x=600//6+150 + x,y=800//3.4+dist+75)
Q2_date_month_input=Entry(root,font=('Arial',10),width=10)
Q2_date_month_input.place(x=600//6+210 + x,y=800//3.4+dist+75)
Q2_date_year=Label(root,text='Year',font=('Arial',10)).place(x=600//6+300 + x,y=800//3.4+dist+75)
Q2_date_year_input=Entry(root,font=('Arial',10),width=10)
Q2_date_year_input.place(x=600//6+350 + x,y=800//3.4+dist+75)
Q2_number_days=Label(root,text='Nr of days',font=('Arial',10)).place(x=600//6 + x,y=800//3.4+dist+140)
Q2_number_days_input=Entry(root,font=('Arial',10),width=10)
Q2_number_days_input.place(x=600//6+75 + x,y=800//3.4+dist+140)

Q2_submit=Button(root,text="Result",command=lambda:Problema2(env, Q2_date_day_input, Q2_date_month_input ,Q2_date_year_input, Q2_number_days_input)).place(x=600//6+450 + x,y=800//7.6+dist+240)


Q3_date_day=Label(root,text='Day',font=('Arial',10)).place(x=600//6 + x,y=800//2+dist+100)
Q3_date_days_input=Entry(root,font=('Arial',10),width=10)
Q3_date_days_input.place(x=600//6+50 + x,y=800//2+dist+100)
Q3_date_month=Label(root,text='Mouth',font=('Arial',10)).place(x=600//6+150 + x,y=800//2+dist+100)
Q3_date_month_input=Entry(root,font=('Arial',10),width=10)
Q3_date_month_input.place(x=600//6+210 + x,y=800//2+dist+100)
Q3_date_year=Label(root,text='Year',font=('Arial',10)).place(x=600//6+300 + x,y=800//2+dist+100)
Q3_date_year_input=Entry(root,font=('Arial',10),width=10)
Q3_date_year_input.place(x=600//6+350 + x,y=800//2+dist+100)
Q3_submit=Button(root,text='Result',font=('Arial',10),command=lambda:Problema3a(env,Q3_date_days_input, Q3_date_month_input, Q3_date_year_input)).place(x=600//6+450 + x,y=800//2+dist+100)
Q3_date_timestamp=Label(root,text='Timestamp',font=('Arial',10)).place(x=600//6 + x,y=900//2+dist+100)
Q3_date_timestamp=Entry(root,font=('Arial',10),width=10)
Q3_date_timestamp.place(x=750//6+50 + x,y=900//2+dist+100)
Q3_submit=Button(root,text='Result',font=('Arial',10),command=lambda:Problema3b(env, Q3_date_timestamp)).place(x=600//6+450 + x,y=900//2+dist+100)
root.mainloop()
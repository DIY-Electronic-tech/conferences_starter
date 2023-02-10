import webbrowser
import time
import datetime

d = datetime.datetime.today()

test = True

url = input(" \n Введите URL: ")
tGo = int(input("Указать время запуска: 1 \nУказать через сколько минут запуск: 2 \n"))
if tGo == 1:
    h = int(input("Во сколько часов запустить: "))
    m = int(input("Во сколько минут запустить: "))
    print("\n Время пошло \n")
    while (test):
        d = datetime.datetime.today()
        if d.minute == m and d.hour == h:
            test = False
            webbrowser.open(url, new = 2, autoraise = True) # new=2, открыть ссылку в новом окне
elif tGo == 2:
    tGo = int(input("Через сколько минут запустить: "))
    print("\n Время пошло \n")
    time.sleep(tGo * 60)
    webbrowser.open(url, new = 2, autoraise = True) # autoraise = True, открыть браузер поверх всех окон
print("Готово!")
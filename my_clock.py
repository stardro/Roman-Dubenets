print("Clock")
run = 1
while run ==1:
    from datetime import datetime, timedelta
    def Time():
        a=datetime(1,1,1) +sec
        print("Дні : часи : минути : секунди")
        print("%d     %d      %d        %d" %(a.day-1, a.hour, a.minute, a.second))
    try:
        sec = timedelta(seconds=int(input("Укажите количество секунд: ")))
        Time()
    except ValueError:
        print("Працюємо тільки з числами!")

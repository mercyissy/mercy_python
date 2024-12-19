import datetime as dt
import pygame

# date_ = dt.datetime.now()
# print(date_.year)
# print(date_.month)
# print(date_.minute)

# mydate = dt.datetime(2025, 1, 1, 12, 00, 00)
# print(mydate)

# print('Alarm..'.center(100))

hour = input('Hour: ').strip()
minute = input('Minute: ').strip()
second = input('Second: ').strip()
am_pm = input('AM/PM: ').strip().upper()

pygame.init()
pygame.mixer.music.load(r"c:\Users\ADMIN\Music\Rema-YAYO-(JustNaija.com).mp3")

while True:
    date_now = dt.datetime.now()

    if date_now.strftime('%H') == hour and date_now.strftime('%M') == minute and date_now.strftime('%S') == second and date_now.strftime('%p') == am_pm:
        print('Alarm is ringing..'.center(100))
        pygame.mixer.music.play()
        pygame.time.wait(10000)
        pygame.mixer.music.stop()

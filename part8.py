
import time


with open('lyrics.txt', 'r') as file:
    lyrics = file.readlines()
    for i in  lyrics:
        time.sleep(0.5)
        print(i.strip())

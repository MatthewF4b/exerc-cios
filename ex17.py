import time as t
import winsound

cont = 10
while cont >= 0:
    print(cont)
    cont -= 1
    t.sleep(2)
    winsound.Beep(3000,100)

print('boooomm')
winsound.Beep(1500,100)

import keyboard
from tkinter import *

r = Tk()
sd =0
bk =0
r.geometry('670x'+str(sd)+'+600+0')
r.attributes("-topmost",True)
r.overrideredirect(1)
r.configure(bg='black')
r.attributes('-alpha', 0.7) 
#650x81+600+0
def nonre():
	global sd
	r.geometry('650x'+str(sd)+'+600+0')
	r.after(5, nonre)
	if sd == 0:
		pass
	else:
		sd -=5
def increase_sd():
	global sd
	global bk
	if bk==1:

		r.geometry('650x'+str(sd)+'+600+0')
		r.after(10, increase_sd)
		if sd == 110:
			pass
			bk=0
		else:
			sd +=5
	else:
		bk=0
		nonre()


def reacroe():
	global bk
	bk=1
	increase_sd()
keyboard.add_hotkey('ctrl+2', reacroe) # добавить горячую клавишу

r.mainloop()
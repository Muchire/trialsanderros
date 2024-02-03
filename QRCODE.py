import pyqrcode
import os,shutil



title = input("give a title :")
text = input("qr code should say?")

filesvg = title + '.svg'
filepng = title+ '.png'


url = pyqrcode.create(text)

url.svg(filesvg, scale= 7)
url.png(filepng, scale= 9)


os.mkdir(fr"C:\Users\user\Desktop\{title}")

shutil.move(f"{filesvg}", fr"C:\Users\user\Desktop\{title}")
shutil.move(f"{filepng}", fr"C:\Users\user\Desktop\{title}")






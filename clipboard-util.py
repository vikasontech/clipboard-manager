import pyperclip
from datetime import datetime as dt
import os

is_print_date = False 
is_append_mode = True

if not os.path.exists('data'):
    os.makedirs('data')

filename=input('Input file name of the[clipboard.txt]:')

if (filename == ''):
  filename = "clipboard.txt"

filename = "./data/"+filename

print(filename)

print("watching clipboard ...")

old = ''
while True:
  try:
    txt = pyperclip.paste()
    if(len(txt) > 0 and old != txt):
      if is_append_mode:
        print('file open in append mode ...')
        f = open(filename, "a+")
      else: 
        print('file open in write mode ...')
        f = open(filename, "a+")
      
      f.write("\n---------------------------------------\n")
      if is_print_date :
        now = dt.now()
        f.write(now.strftime("%d/%m/%Y %H:%M:%S")+"\n")
      print('writing in file')
      f.write(txt)
      old = txt
      print(old)
      f.close()
      
  except KeyboardInterrupt as e:
    exit()

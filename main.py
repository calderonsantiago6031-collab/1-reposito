import random
import time

eng_word = ['hi','bay','task','program']
sp_words = ['hola','adios','tarea','programa']
score = 0

mode = input("elije un modo : 0 - añadir nuevas palabras, 1 - entretenimiento: /n")
while ((mode != '0') and (mode != '1')):
  mode = input("simbolo no balido eleji 0 o 1 (0 añade nuevas palabras , 1 perminte el entretenimiento) /n")

if mode == "1":
  print("¡traduce tantas palabras como puedas! ¡tienes 10 intentos!")
  for i in range(10):
    
       

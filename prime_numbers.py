# -*- coding: utf-8 -*-
"""prime-numbers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ptoaMsmCLUWC4IBL5eFs6LV9ZGiDoewU
"""

n = int(input("Enter a number: "))

prime = True


if n == 1:
  print(str(n) + " is not prime")
  prime = False

for i in range(2, n):
  if n % i == 0:
    prime = False
    print(str(n) + " is not prime")
    break
  else:
    continue
  

if prime == True:
  print(str(n) + " is prime")

n = int(input("Enter a number:"))

prime = True

if n == 1:
  print(str(n) + " is not prime")
  prime = False

for i in range(2, n):
  if n % i == 0:
    print(str(n) + " is not prime")
    prime = False
    break
  else:
    continue

if prime == True:
  print(str(n) + " is prime")
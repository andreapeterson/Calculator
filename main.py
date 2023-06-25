import os
def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
from art import logo
import math
#Add
def add(n1,n2):
  return n1+n2
#Subtract
def subtract(n1,n2):
  return n1-n2
#Multiply
def multiply(n1,n2):
  return n1*n2
#Divide
def divide(n1,n2):
  return n1/n2
#exponent
def exponent(n1,n2):
  return n1**n2
#squareroot
def squareroot(n1):
  return math.sqrt(n1)


calc_dict={"+":add,
"-":subtract, 
"*":multiply, 
"/":divide, 
"^":exponent,
"sqrt":squareroot}

def calculator():
  print(logo)
  num1= float(input("What is the first number?: "))
  
  
  for symbol in calc_dict:
    print (symbol)
  
  keep_going=True
  while keep_going:
    op=input("Pick an operation: ")
    if op != "sqrt":
      num2= float(input("What is the next number?: "))
    
    def my_calculator():
      if op=="+":
        answer=add(num1, num2)
      if op=="-":
       answer=subtract(num1, num2)
      if op=="*":
        answer=multiply(num1, num2)
      if op=="/":
        answer=divide(num1, num2)
      if op=="^":
        answer=exponent(num1, num2)
      if op=="sqrt":
        answer=squareroot(num1)
      return answer
    
    if op == "sqrt":
      print(f"{op} {num1} = {my_calculator()}")
    else:
      print (f"{num1} {op} {num2} = {my_calculator()}")
      
    if input(f"Type 'y' to continue calculating with {my_calculator()} or type 'n' to start a new calculation: ") == "y":
      num1=my_calculator()
    else: 
      keep_going=False
      clear()
      calculator()
    
    
  


calculator()



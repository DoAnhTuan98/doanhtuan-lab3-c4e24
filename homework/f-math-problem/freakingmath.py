from random import *








def generate_quiz(): # lay bieu thuc ngau nhien
    # Hint: Return [x, y, op, result]
  
    x = randint(1,10)  
    y = randint(1,10)  
    op = "+"
    error  = randint(-1,1)
    
    if op == "+":
        result = x + y +error
    
    
    return x, y, op, result


    


    


def check_answer(x, y, op, result, user_choice):
    
    
    # generate_quiz()

    # a = generate_quiz()
    # print(a)
    # print(user_choice)
 
    # if op == "+":
    #     result = x + y +error
    # elif op == "-":
    #     result = x - y +error
    # elif op == "*":
    #     result = x * y +error
    # elif op == "/":
    #     result = x/y+error
    if user_choice == True:
        if result == x + y:
            return True
        else:
            return False
    elif user_choice == False:
        if result != x+y:
            return True
        else:
            return False


       

    
   
    
    
       
    

    

def add(a,b):
    add_result = a + b 
    return add_result

def sub(a,b):
    sub_result = a - b
    return sub_result

def mul(a,b):
    mul_result = a * b 
    return mul_result


def div(a,b):
    if((a==0 and b == 0 )or (b==0)):
        raise ValueError("ZeroDivisionError, float division by zero")

    else:
        return a/b

#a,b  = map(float,input().split(","))
#print(" Addition : ",round(add(a,b),3),"\n","Subtraction: ",round(sub(a,b),2),'\n',"Multiplication : ",round(mul(a,b),2),'\n',"Division : ",div(a,b))
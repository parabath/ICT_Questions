def fun(para1,para2):
    x=foo(para2,para1)
    return x
def foo(para3,para4):
    return para3-para4

result=fun(2,4)
print("Result is"+str(result))
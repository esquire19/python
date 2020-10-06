f = 0 
def fact(num):
  globle num
  if(num==1):
    return 1
  f = f*fact(num-1)
  return f
print(fact(5))

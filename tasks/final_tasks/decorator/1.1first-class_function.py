#Understanding the first-order functions

def shout(text): 
    return text.upper() 
  
print (shout('Hello')) 
  
yell = shout 
  
print (yell('Hello')) 
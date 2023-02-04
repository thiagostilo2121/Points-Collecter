#Function

def genPass(base: str, passLong: int):
    import random

    if not type(base) == str: 
      raise TypeError("`base` is not a string! Error code: 1-001 A")
      return

    if not type(passLong) == int: 
      raise TypeError("`passLong` is not a int! Error code: 1-001 B")
      return  

    try:
       password = random.sample(base, passLong)
       print(password)
    except Exception as error:
       print("Error has ocurred!", error) 

#Example:

    
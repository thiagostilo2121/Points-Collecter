#Function 
def randomPass(Ñ: bool):
    import random
 
    if not isinstance(Ñ, bool):
        raise TypeError("`Ñ` is not boolean! Error code 1-001 C")
        return
    
    '''
    :param Ñ: The password contain "Ñ"? True = yes -- False = no
    '''

    try:
        if Ñ == True:
          min = "abcdefghijklmnñopqrstuvwxyz"
          may = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        else:
            min = "abcdefghijklmnopqrstuvwxyz"
            may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = "0123456789"    
        
        base = min + may + num

        passLong = random.randint(8, 15)

        password = random.sample(base, passLong)

        print(password)
    except Exception as error:
        print("Error has ocurred", error) 

#Example

randomPass(True)
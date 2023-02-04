def setData(name: str, content: str, type_lo: str):
    import random
    import os 
    if not type(name == str):
        raise TypeError("`name` is not a string! Error Code: 1-001 E")
        return
    if not type(content == str):
        raise TypeError("`content` is not a string! Error Code: 1-001 F") 
        return
    if not type(type_lo == str):
         raise TypeError("`type_lo` is not a string! Error Code: 1-001 G") 
         
    if not type_lo ==  "w":
        if not type_lo == "a":
                    raise TypeError(type_lo, "is not supported, try with a or w")   
                    return 

    if os.path.exists(f"{name}.txt") == False:
        raise TypeError("The file dosen't exist")   
        return
        
    with open(f"{name}.txt", type_lo) as local:
           local.write(f"\n{content}")

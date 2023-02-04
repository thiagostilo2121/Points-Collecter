def readData(name: str):
    import os
    if not type(readData == str):
        raise TypeError("`name` is not a string! Error Code: 1-001 E")

    if os.path.exists(f"{name}.txt") == False:
         raise TypeError("The file dosen't exist")
         return        

    with open(f"{name}.txt", "r") as local:
        read = local.read()
        print(read)




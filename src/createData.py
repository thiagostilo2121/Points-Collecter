def createData(name: str):
    import os
    import random
    if not type(name == str):
        raise TypeError("`name` is not a string! Error code: 1-001 E")
        return
    path_file = os.path.exists(f"{name}.txt") 

    if path_file == True: 
        raise TypeError("The file already exist")
        return

    with open(f"{name}.txt", "a")  as local:
      local.write(f"Data %{name}% > info {local}")

    
        
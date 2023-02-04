def removeData(name: str):
    import os
    if not type(name == str):
        raise TypeError("`name` is not a string! Error Code: 1-001 E")
        return
        
    if os.path.exists(f"{name}.txt") == False:
        raise TypeError("The file dosen't exist")
        return    
    os.remove(f"{name}.txt")    
    print(f"data %{name}% removed")

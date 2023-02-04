def setTxt(args: str):
    if not isinstance(args, str):
        raise TypeError("`args` is not a string! Error code: 1-001 D")
        return

    try:
        import os
        print("No supported!, comming soon")
        return
    except Exception as error:
        print("Error as ocurred!", error)    

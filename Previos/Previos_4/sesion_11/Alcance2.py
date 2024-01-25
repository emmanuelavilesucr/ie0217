def outer():
    message = "local"
    
    def inner():
        
        nonlocal message
        
        message = "nonlocal"
        
        print("inner:", message)
        
    inner()
    print("outer:", message)
    
outer()
def outer_function():
    num = 20  # Variable local 
    
    def inner_function():
        global num
        num = 25 # Modifica la variable
    
    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)
    
    
outer_function()
print("Outside both function: ", num)
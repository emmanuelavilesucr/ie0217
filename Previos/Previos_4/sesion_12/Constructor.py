class Point(object):
    
    def __new__(cls, *args, **kwargs):
        print("From new")
        print(cls)
        print(args)
        print(kwargs)
        
        # Llama al metodo new para crear una nueva instancia
        obj = super().__new__(cls)
        return obj
    
    # Metodo constructor que inicializa los atributos de la instancia
    def __init__(self, x = 0, y = 0):
        print("From init")
        # Inicializa atributos
        self.x = x
        self.y = y

class SqPoint(Point):
    MAX_Inst = 4  # Numero maximo de instancias 
    Inst_created = 0 # Cuenta las instancias creadas
    
    def __new__(cls, *args, **kwargs):
        if (cls.Inst_created >= cls.MAX_Inst):
            raise ValueError("Cannot create more objects")
        cls.Inst_created += 1  # Incrementa el contador de instancias
        
        return super().__new__(cls) # Llama al método new para crear una nueva instancia
class A:
    
    def __init__(self,a_val):
        print("Initialize new instance of A")
        self.a_value=a_val
        
class B:
    
    def __new__(cls,*args,**kwargs) :
        return A(2)
    def __init__(self,b_val) -> None:
        self.b_value=b_val
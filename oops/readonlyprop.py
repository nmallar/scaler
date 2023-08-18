class WritePropertyException(Exception):
    
    pass

class Point:
    
    def __init__(self,x,y) -> None:
        self._x=x
        self._y=y
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @x.setter
    def x(self,val):
        raise WritePropertyException(f"x is  a read only property")
    @y.setter
    def y(self,val):
        raise WritePropertyException(f"y is a read only property")
    
class Circle:
    def __init__(self, radius) -> None:
        self._radius=radius        
    @property
    def radius(self):
        """This is the radius property"""
        return self._radius
        
    @radius.setter
    def radius(self,value):
        self._radius=value
        
    @radius.deleter
    def radius(self):
        del self._radius
    
    
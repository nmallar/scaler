class Circle:
    def __init__(self,radius) -> None:
        self._radius=radius
    
    
    def _get_radius(self):
        print("Getting radius")
        return self._radius
    def _set_radius(self,value):
        print("Setting Radius")
        self._radius=value
    def _del_radius(self):
        print("Deleting radius")
        del self._radius
    radius=property(fget=_get_radius,fset=_set_radius,fdel=_del_radius, doc="Radius prop")
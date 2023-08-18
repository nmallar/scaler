class Distance(float):
    def __new__(cls,value,unit):
        instance=super().__new__(cls,value)
        instance.unit=unit
        return instance
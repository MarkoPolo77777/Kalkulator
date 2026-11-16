class Calculator:
    def __init__(self, op1: float, op2: float):
        self.__op1 = op1
        self.__op2 = op2
    def sum(self) -> float: 
        if not isinstance(self.__op1, (int, float)) or not isinstance(self.__op2,(int, float)):
            raise TypeError("Nieprawdiłowa wartość")
        return self.__op1 + self.__op2
    def subtract(self) -> float:
        if not isinstance(self.__op1, (int, float)) or not isinstance(self.__op2,(int, float)):
            raise TypeError("Nieprawdiłowa wartość")
        return self.__op1 - self.__op2
    def multiply(self) -> float:
        if not isinstance(self.__op1, (int, float)) or not isinstance(self.__op2,(int, float)):
            raise TypeError("Nieprawdiłowa wartość")
        return self.__op1 * self.__op2
    def divide(self) -> float | None:
        try:
            if not isinstance(self.__op1, (int, float)) or not isinstance(self.__op2,(int, float)):
                raise TypeError("Nieprawdiłowa wartość")
            value = self.__op1 / self.__op2    
        except ZeroDivisionError:
            return None
        else:
            return value
c1 = Calculator(-10, 2)
c2 = Calculator(0, 1.5)
c3 = Calculator(2, 1)
print(c1.sum(), c1.multiply(), c1.divide())
print(c2.divide(), c2.subtract())
print(c3.divide(), c3.subtract())

        
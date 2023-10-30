#EJERCICIO 1

class Person:
    def __init__(self, name = None, age = None, dni = None):
        self.name = name
        self.age = age
        self.dni = dni

    def set_name(self, name):
        self.__name = name.capitalize()

    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        if age < 0:
            print("La edad no puede ser negativa")
        else:
            self.__age = age

    def get_age(self):
        return self.__age
    
    def set_dni(self, dni):
        if len(str(dni)) < 7:
            print("Ingrese un DNI válido")
            self.set_dni(int(input()))
        else:
            self.__dni = dni

    def get_dni(self):
        return self.__dni
    
    def show_person(self):
        print("Nombre: ", self.__name)
        print("Edad: ", self.__age)
        print("DNI: ", self.__dni)

    def is_of_age(self):
        if self.__age < 18:
            return False
        else:
            return True

### USO DE CLASE PERSON ###
person1 = Person()
person1.set_name(input("Ingrese su nombre: "))
person1.set_age(int(input("Ingrese su edad: ")))
person1.set_dni(int(input("Ingrese su DNI: ")))
print("¿Es ", person1.get_name(), " mayor de edad? ", person1.is_of_age())


#EJERCICIO 2
class Account:
    def __init__(self, owner, quantity = 0.0):
        self.owner = owner
        self.quantity = quantity
    
    def set_owner(self, owner):
        self.__owner = owner
    
    def get_owner(self):
        return self.__owner

    def set_quantity(self, quantity):
        self.__quantity = quantity
    
    def get_quantity(self):
        return self.__quantity
    
    def show_account(self):
        print("TITULAR: ", self.owner)
        print("SALDO: $", self.quantity)
    
    def enter_money(self, quantity):
        if quantity > 0:
            self.quantity += quantity
    
    def withdraw_money(self, quantity):
        if quantity > 0:
            self.quantity -= quantity

### USO DE CLASE ACCOUNT ###
account1 = Account("Juan Perez", 500.0)
account1.show_account()
account1.enter_money(1400.0)
account1.withdraw_money(300.0)
account1.show_account()

#EJERCICIO 3
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def print_largest_side(self):
        print("El lado mayor es el de ", max(self.side1, self.side2, self.side3), " cm") 
    
    def triangle_type(self):
        if self.side1 == self.side2 and self.side2 == self.side3:
            print("ES UN TRIÁNGULO EQUILÁTERO")
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            print("ES UN TRIÁNGULO ISÓCELES")
        else:
            print("ES UN TRIÁNGULO ESCALENO")

    #SETTERS
    def set_side1(self, side1):
        if side1 > 0:
            self.__side1 = side1
    
    def set_side2(self, side2):
        if side2 > 0:
            self.__side2 = side2
    
    def set_side3(self, side3):
        if side3 > 0:
            self.__side3 = side3
    
    #GETTERS
    def get_side1(self):
        return self.__side1
    
    def get_side2(self):
        return self.__side2
    
    def get_side3(self):
        return self.__side3

###USO CLASE TRIANGLE###
triangle = Triangle(4,5,5)
triangle2 = Triangle(10,8,4)
triangle3 = Triangle(7,7,7)
triangle.triangle_type()
triangle.print_largest_side()
triangle2.triangle_type()
triangle3.triangle_type()
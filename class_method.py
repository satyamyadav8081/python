class instructer:
    followers=0  #CLASS OBJECTN  VVARIABLE 
    def __init__ (self,name,address):
        self.name=name
        self.addres=address
       #self.followers=0

    def display(self):
        print("hi")

instructer_1=instructer("satyam","ghosi")
print(instructer_1.name)
print(instructer_1.display())





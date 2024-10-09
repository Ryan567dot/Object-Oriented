class Coffee:
    milk = 50
    Coffee = 50
    
cap = Coffee()
print(cap.milk)

#Init

class Car:
    def _init_(self,name,model,price,seats,AC):
        self.Name = name
        self.Model = model
        self.Price = price
        self.Seats = seats
        self.AC = AC
        
bmw = Car("BMW","V8","40000$",6,True)
suzuki = Car("Suzuki","A2","200$",4,False)

print(bmw.Price)
print(suzuki.Model)

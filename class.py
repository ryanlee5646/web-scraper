class Car():
    
    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black") # kwargs.get(key, default)
        self.price = kwargs.get("price", "$20")
    
    def __str__(self):
        return f"Car with {self.wheels} wheels"

# Car 클래스를 상속
class Convertible(Car):

    def __init__(self,**kwargs): 
        # super()을 선언하면 부모클래스의 메서드를 상속, 선언하지 않으면 오버라이드 
        super().__init__(**kwargs) # **kwarg를 선언하지 않으면 default값, 선언하면 객체 생성시 넘겨준 argument값을 받아옴
        self.time = kwargs.get("time", 10)

    def take_off(self):

        return "taking off"        

    def __str__(self):
        return f"Car with no roof"


porche = Convertible(color="green", price="$40")
mini = Car()

print(porche.color, porche.price)
porche.take_off()
 
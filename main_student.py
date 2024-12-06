class Student:
    def sleep(self):
        print(f'{self.name}, уснул в автобусе!')

    def __init__(self, pay, name):    
        self.name = name
        self.pay = pay
        print(f'{self.name}, вышел из дома')
        print(f'{self.pay}тг - стоимость проезда на автобусе до Университета по Оңай')

student = Student(pay=100, name='Андрей')

student.sleep()
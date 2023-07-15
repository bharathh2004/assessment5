
#Challenge 1: Square Numbers and Return Their Sum

# class Point:

#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def sqsum(self):
#         print(self.x**2 + self.y**2 + self.z**2) 
       
# obj = Point(1,3,5)
# obj.sqsum()




# class Calculator:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def add(self):
#         print(self.x + self.y)
#     def subtract(self):
#         print(self.x - self.y)
#     def multiply(self):
#         print(self.x * self.y)
#     def divide(self):
#         print(self.x % self.y)
# obj = Calculator(10, 94)
# obj.add()
# obj.subtract()
# obj.multiply()
# obj.divide()



# Challenge 3: Implement the Complete Student Class

# class Student:

#     def __init__(self):
#         self.__name = "bharath"
#         self.__rollno = 123   
#     def getname(self):
#         return self.__name
#     def getrollno(self):
#         return self.__rollno     
#     def setname(self,new_name):
#         self.__name = new_name
#     def setrollno(self,new_rollno):    
#         self.__rollno = new_rollno    
    
# c = Student()   
# print(c.getname())
# c.setname("bala")
# print(c.getname())
# print(c.getrollno())
# c.setrollno(321)
# print(c.getrollno())



#Challenge 4: Implement a Banking Account

# class Account:

#     def __init__(self,title,balance):
#         self.title = title
#         self.balance = balance

#     def fun(self):
#         print(self.title,self.balance)    
        

# class SavingsAccount(Account):
#     def __init__(self,title,balance,interest):
#         super().__init__(title,balance)
#         self.interest = interest

#     def total_balance(self):
#         print(self.title,self.balance,self.interest)


# savings1 = SavingsAccount("Ashish",5000,5)
# savings1.total_balance()    





#Challenge 5: Handling a Bank Accoun

# class Account:
#     def __init__(self, title, balance):
#         self.title = title
#         self.balance = balance  
    
#     def withdrawal(self, drawings):
#         self.drawings = drawings
#         print(self.balance - self.drawings)
         
         

#     def deposit(self, amount):
#         self.amount = amount
#         print(self.balance + self.amount)

#     def getBalance(self):
#         self.__balance = 2000
    
# class SavingsAccount(Account):
#     def __init__(self, title, balance, interestRate):
#             super().__init__(title, balance)
#             self.interestRate = interestRate
    
#     def interestAmount(self):
#         print((self.interestRate*self.balance)//100)

# object = SavingsAccount("bala",2000,5)        
# object.interestAmount()
# object.withdrawal(500)
# object.deposit(500)
# object.getBalance()

































    
      
Create a real time scenario for inheritance example Banking concept

ANSWER:
class Bank1:
    def f(self):
        input("Enter Your Name :")

class ACCOUNT(Bank1):
    def f1(self):
        input(" Account Number :")
class IFSC(ACCOUNT):
    def f2(self):
        input("IFSC CODE :")
class Branch(Bank1):
    def f3(self):
        input(" Branch Name:")
class amount(Bank1):
    def f4(self):
        input("Enter Amount You Want to Deposit :")
        print("Payment Successful")
        print("Thankyou!!")
        

m=Bank1()
n=ACCOUNT()
o=IFSC()
p=Branch()
q=amount()
m.f()
n.f1()
o.f2()
p.f3()
q.f4()

OUTPUT:

Enter Your Name :Jesuv
Account Number :52637262
IFSC CODE :VF6789BG
Branch Name:Anna Nagar
Enter Amount You Want to Deposit :2000
Payment Successful
Thankyou!!

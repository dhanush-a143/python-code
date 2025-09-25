print("start pannita da ")
x=10
y=90
print(x+y)


age=20
print(age,type(age))

# printSomeThing - camal case
# PrintSomeThing - pascal case
# print-some-thing - kebab case
# print_some_thing - snake case


price=99.99
print (price,type(price))

name='dhanush'
print(name,type(name))

csk_win=True
print(csk_win,type(csk_win))

address=None
print(address,type(address))





x=100
x="name"
x=4.7
print(x)




# L # E # G # B

# local variable

def local():
    name="Thar"
    print("my favarate car is:",name)

local()

# Enclosing variable

def enclose_1():
    car="mahendra"

    def enclose_2():
     print("the car company is:",car)

     enclose_2()

enclose_1()


# global variable

cars="Thar"
def car_1():
      print("this is my car:",cars)

      def car_2():
       print("my car is black color:",cars)

      car_2()


car_1()


# builtin variable

print(__file__)

# example usecase for l e g b


cars="showroom"

def black():
    car_1="mahendra thar"

    def white():
        car_2="scarfio"

        print(" i buy {car_1} and {car_2} from{cars}")

        white()
        black()


      




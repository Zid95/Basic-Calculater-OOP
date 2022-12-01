class Calc:

    def __init__(self):
        while True:
            user_menu = input('''
What Do You Want To Do?

"A" => Addition
"S" => Subtraction
"M" => Multiplication
"D" => Division
"E" => Exit

please Choose The Letter? 
''').upper()

            if user_menu == "A":
                a = int(input("Enter The First Number: "))
                b = int(input("Enter The Second Number: "))
                result_add = self.add(a, b)
                print(f"{a} + {b} = {result_add}")

            elif user_menu == "S":
                a = int(input("Enter The First Number: "))
                b = int(input("Enter The Second Number: "))
                result_sub = self.sub(a, b)
                print(f"{a} - {b} = {result_sub}")

            elif user_menu == "M":
                a = int(input("Enter The First Number: "))
                b = int(input("Enter The Second Number: "))
                result_mul = self.mul(a, b)
                print(f"{a} x {b} = {result_mul}")

            elif user_menu == "D":
                a = int(input("Enter The First Number: "))
                b = int(input("Enter The Second Number: "))
                result_div = self.div(a, b)
                print(f"{a} ÷ {b} = {result_div}")

            elif user_menu == "E":
                self.close()

    def add(self, a, b):

        return a + b

    def sub(self, a, b):

        return a - b

    def mul(self, a, b):

        return a * b

    def div(self, a, b):

        return a / b

    def close(self):

        print("Calculater Ended")

        quit()


c = Calc()

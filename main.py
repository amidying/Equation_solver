
class Equation:
    name = "Ali Neaz"
    school ="Islamic University,Kushtia"
    department = "Statistics"

    def __init__(self,yourname):
        self.yourname = yourname
    
    def evaluate(self,x,eqn):
        self.x = x
        return eval(self.eqn)


if __name__ == "__main__":
    print("Wellcome to my equation solver.")
    run = True
    while run:
        print("Enter the method you want: ")
        print("1. Bisection Method")
        print("2. Regular Falsi Position")
        print("3. Newton Raphson Method")
        print("4. Evaluate the equation")
        print("5. To quit")
        choice = input()
        if choice == "1":
            eqn = input("Enter your equation: ")
            ans = Equation(eqn)
            print(f"Your ans for the equation {eqn} is: {ans}")
        elif choice == "4":
            eqn = input("Enter your equation: ")
            x = float(input("Enter your x\n"))
            print(Equation.evaluate(x,eqn))
        elif choice == "q":
            run = False
    print("Thank you for using my code.")
        

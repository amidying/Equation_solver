
class Equation:
    name = "Ali Neaz"
    school ="Islamic University,Kushtia"
    department = "Statistics"

    def __init__(self,yourname):
        self.yourname = yourname
        
    
    def evaluate(self,x,eqn):
        self.x = x
        self.eqn = eqn
        return eval(self.eqn)
    def introduceCalculator(self):
        print("________________________________________________________________________________________________________________")
        print(f"Hi this is Ali Neaz . I am a student of department of department of Statistics at Islamic University, Kushtia.")
        print("________________________________________________________________________________________________________________")


if __name__ == "__main__":
    print("_______________________Wellcome to my equation solver_______________________")
    print("Enter your name: ")
    name = input()
    run = True
    while run:
        print("Enter the method you want: ")
        print("1. Bisection Method")
        print("2. Regular Falsi Position")
        print("3. Newton Raphson Method")
        print("4. Evaluate the equation")
        print("5. To quit")
        print("6. Introduce Calculator")
        choice = input()
        eqns = Equation(name)
        if choice == "1":
            eqn = input("Enter your equation: ")
            ans = Equation(eqn)
            print(f"Your ans for the equation {eqn} is: {ans}")
        elif choice == "4":
            eqn = input("Enter your equation: ")
            x = float(input("Enter your x: "))
            print(eqns.evaluate(x,eqn))
        elif choice == "6":
            eqns.introduceCalculator()
        elif choice == "5":
            run = False

    print("Thank you for using my code.",name)
    print("_______________________Do Come Agein_______________________")
        


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
        # print(f"Hi this is Ali Neaz . I am a student of department of department of Statistics at Islamic University, Kushtia.")
        print(f"Hi this is {self.name}. I am a student of {self.department} at {self.school}")
        print("________________________________________________________________________________________________________________")
    def bisection(self,n,eqn):
        self.n = n
        a = self.calc_a(eqn)
        b = self.calc_b(eqn)
        run = True
        cnt = 0
        while run:
            x = (a+b)/2
            cnt += 1
            if self.evaluate(x,eqn) > 0:
                b = x
            else:
                a = x

            if cnt == self.n:
                run = False
        print(f"The root for {self.n} iteration is: {x}")

    def regularFalsi(self,a,b,eqn):
        pass
    def newtonRaphson(self,a,b,eqn):
        pass

    def calc_a(self,eqn):
        self.eqn = eqn
        for i in range(-10,10):
            if self.evaluate(i,eqn) < 0:
                return i
        print("Sorry the range overflowed.")
        return None
    def calc_b(self,eqn):
        for i in range(-10,10):
            if self.evaluate(i,eqn) > 0:
                return i
        print("Sorry the range overflowed.")
        return None



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
        print("5. Introduce Calculator")
        print("6. To quit")
        print("7. Whoami?")
        choice = input()
        eqns = Equation(name)
        if choice == "1":
            eq = input("Enter your equation: ")
            n = int(input("Enter number of iterations: "))
            eqns.bisection(n,eq)
        elif choice == "4":
            eqn = input("Enter your equation: ")
            x = float(input("Enter your x: "))
            print(eqns.evaluate(x,eqn))
        elif choice == "5":
            eqns.introduceCalculator()
        elif choice == "6":
            run = False
        elif choice=="7":
            print(f"You ar {name} and we are happy that you are using our code.")
            print("Thank you.")

    print("Thank you for using my code.",name)
    print("_______________________Do Come Agein_______________________")
        

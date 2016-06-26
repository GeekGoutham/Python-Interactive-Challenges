#Author = Vignesh Goutham

class factorial:
    def __init__(self, number):
        self.fact_number = number
        self.result = 1

    def compute_fact(self):
        if self.fact_number == 0:
            self.result = 1
        while self.fact_number > 0:
            self.result *= self.fact_number
            self.fact_number -= 1
        return self.result

    def compute_Fact_recursion(self, number):
        if number == 0:
            return 1
        else:
            result = number * self.compute_Fact_recursion(number - 1)
        return result

if __name__ == "__main__":
    fact = factorial(0)
    res = fact.compute_Fact_recursion(3)
    print(res)
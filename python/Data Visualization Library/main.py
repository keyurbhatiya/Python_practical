# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

class InterestCalculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

class SimpleInterest(InterestCalculator):
    def calculate(self):
        return self.principal * (1 + (self.rate / 100) * self.time)

class CompoundInterest(InterestCalculator):
    def calculate(self):
        return self.principal * (1 + (self.rate / 100)) ** self.time

def plot_interest(principal, rate, max_time):
    times = np.arange(1, max_time + 1)
    simple_interest_values = []
    compound_interest_values = []

    simple_interest_calculator = SimpleInterest(principal, rate, max_time)
    compound_interest_calculator = CompoundInterest(principal, rate, max_time)

    for t in times:
        simple_interest_values.append(simple_interest_calculator.calculate())
        compound_interest_calculator.time = t  # Update time for compound interest
        compound_interest_values.append(compound_interest_calculator.calculate())

    plt.figure(figsize=(10, 6))
    plt.plot(times, simple_interest_values, label='Simple Interest', marker='o')
    plt.plot(times, compound_interest_values, label='Compound Interest', marker='x')
    plt.title('Simple Interest vs Compound Interest')
    plt.xlabel('Time (years)')
    plt.ylabel('Amount (₹)')
    plt.legend()
    plt.grid()
    plt.show()

# Example usage
if __name__ == "__main__":
    principal_amount = 1000  # Principal amount
    interest_rate = 5        # Interest rate in percentage
    max_time_period = 10     # Time period in years

    plot_interest(principal_amount, interest_rate, max_time_period)
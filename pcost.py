"""

AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44

Data/portfolio.dat 
"""

# Read a dat file
print('hello')

import fileinput


def portfolio_cost(filename: str) -> float:
    total_cost = 0.0
    for line in fileinput.input(filename):
        try:
            record = line.split()
            total_cost = total_cost + int(record[1])*float(record[2])
        except ValueError as e:
            print(f"Couldn't parse line: {repr(line)}")
            print(f"Reason: {e}")
    
    return total_cost

print(portfolio_cost('Data/portfolio3.dat'))

# if __name__ == "__main__":
#     print(portfolio_cost('Data/portfolio3.dat'))

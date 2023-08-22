import math
from tabulate import tabulate

# Real GDP Calculator Using Chain-Weighted Real GDP Growth

def main():
    instructions()
    p = get_prodnum()
    n = set_name(p)
    y = int(get_year())

    data = Data_Storage(p, n, y)
    year1 = data.set_data()
    get_table(y, n, year1)

    data2 = Data_Storage(p, n, y+1)
    year2 = data2.set_data()
    get_table(y+1, n, year2)

    result1, result2 = calculator(year1, year2)
    print(f"Chain Weighted Real GDP for {y}: {result2}")
    print(f"Chain Weighted Real GDP for {y+1}: {result1}")

# Stores number of products produced and sold and price for each year
class Data_Storage():

    # Constructor
    def __init__(self, product, name, year):
        self._name = name
        self._amount = ""
        self._cost = ""
        self._data = {}
        self._product = product
        self._year = year

    # Setter
    def set_data(self):
        print(f"Beginning Data Entry for {self._year}:")
        data = {}
        for i in range(self.product):
            print(f"For Product {self.name[i]}:")
            while True:
                try:
                    self._amount = input("How many were produced and sold: ")
                    self._amount = int(self._amount)
                    break
                except ValueError:
                    print("Please Enter a Valid Integer")
            while True:
                try:
                    self._cost = input("Cost of each item: ")
                    self._cost = float(self._cost)
                    break
                except ValueError:
                    print("Please Enter a Valid Cost")
            self._data.update({self.name[i]: [self._amount, self._cost]})
        return self._data

    # Getters
    def get_name(self):
        return self.name

    def get_amount(self):
        return self._amount

    def get_cost(self):
        return self._cost

    def get_data(self):
        return self._data

    def get_year(self):
        return self.year

    # Properties
    @property
    def name(self):
        return self._name

    @property
    def amount(self):
        return self._amount

    @property
    def cost(self):
        return self._cost

    @property
    def data(self):
        return self._data

    @property
    def year(self):
        return self.year

    @property
    def product(self):
        return self._product

# Gets Set Number of Product Numbers
def get_prodnum():
    while True:
        try:
            p = int(input("Input number of products: "))
            break
        except ValueError:
            print("Please enter a valid integer")
    return p

# Sets name for each product
def set_name(p):
    name = []
    for i in range(p):
        name.append(input(f"The Name of Product #{i+1} is: "))
    return name

# Get years for which Real GDP is calculated
def get_year():
    while True:
        try:
            year = input("Year for this data is: ")
            int(year)
            return year
        except ValueError:
            print("Invalid Year")

# Calculates Real GDP for each year
def calc_rgdp(this_year, base_year):
    p1 = list(this_year.keys())
    p2 = list(base_year.keys())
    rgdp = 0
    for i in range(len(list(this_year.keys()))):
        rgdp += float(this_year[p1[i]][0]) * float(base_year[p2[i]][1])
    return rgdp

# Calculates the Real GDP Growth
def calc_rgdp_growth(rgdp_this, rgdp_last):
    return rgdp_this/rgdp_last

# Calculates chain rate by taking geometric average of two years
def calc_chain_rate(growth_rate1, growth_rate2):
    return round(math.sqrt(growth_rate1 * growth_rate2), 2)

# Calculates Real GDP using chain weight rates
def calc_chain_rgdp(rgdp_last, rgdp_this, chain_rate):
    return rgdp_last*chain_rate, rgdp_this/chain_rate

# Calculates Chain Weighted Real GDP for both years using functions above
def calculator(year1, year2):
    rgdp1 = calc_rgdp(year1, year1)
    rgdp2 = calc_rgdp(year2, year1)
    print("Real GDP Using Last Year as Base Year: ")
    print(f"Last Year: {rgdp1} | This Year: {rgdp2}")
    growth1 = round(calc_rgdp_growth(rgdp2, rgdp1), 2)
    print(f"Real GDP Growth Rate (Last Year as Base Year): {growth1}")
    rgdp3 = calc_rgdp(year1, year2)
    rgdp4 = calc_rgdp(year2, year2)
    print("Real GDP Using This Year as Base Year: ")
    print(f"Last Year: {rgdp3} | This Year: {rgdp4}")
    growth2 = round(calc_rgdp_growth(rgdp4, rgdp3), 2)
    print(f"Real GDP Growth Rate (This Year as Base Year): {growth2}")
    chain = calc_chain_rate(growth1, growth2)
    print(f"Chain Weighted Growth Rate: {chain}")
    chain_this, chain_last = calc_chain_rgdp(rgdp1, rgdp4, chain)
    chain_this = round(chain_this, 2)
    chain_last = round(chain_last, 2)
    return chain_this, chain_last

# Sets data into a visible table
def see_data(year, n, data):
    r0 = [year]
    for _ in range(len(n)):
        r0.append("")
    r1 = ['Products']
    for i in range(len(n)):
        r1.append(n[i])
    r2 = ['Amount']
    r3 = ['Cost']
    p1 = list(data.keys())
    for i in range(len(list(data.keys()))):
        r2.append(data[p1[i]][0])
        r3.append(data[p1[i]][1])
    table = [r0, r1, r2, r3]
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

# Gives user option to see data in a table, if yes, creates and returns table
def get_table(y, n, data):
    while True:
        user = input("See data in a table? (y/n): ")
        if user == "y":
            return see_data(y, n, data)
        elif user == "n":
            break
        else:
            print("Please enter 'y' for yes and 'n' for no")

# Gives instruction to user
def instructions():
    while True:
        user = input("Would you like to see the instructions? (y/n): ")
        if user == "y":
            print("Welcome to the Chain Weighted Real GDP Calculator!")
            print()
            print("You will now be asked to input data of the economy for 2 consecutive years.")
            print()
            print("Starting with data for a specific year and then the year after that.")
            break
        elif user == "n":
            break
        else:
            print("Please enter 'y' for yes and 'n' for no")

if __name__ == "__main__":
    main()



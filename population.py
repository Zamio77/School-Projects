"""
A program to pull the numbers from a file
and display them in a list. The output
calls for the change in the populations,
not the actual population numbers.
"""
import math

def pop_list():

    # open the list
    pop = open('USPopulation.txt', 'r')

    # read the contents into a list
    population = pop.readlines()

    # create the loop to read into list
    index = 0
    while index < len(population):
        population[index] = int(population[index].rstrip('\n'))
        index += 1

    return population

def year():
    # Create the year list
    years = []

    first = 1950

    # Loop through the years for the list
    for i in range(41):
        years.append(first)
        first += 1

    return years

def change(population):

    # Create the empty list
    pop_change = []

    # subtract the numbers to find the change
    for v, w in zip(population[:-1], population[1:]):
        change = w - v
        pop_change.append(change)

    return pop_change
    
def calculations(pop_change, years):

    # Calculate the average
    avg_change = sum(pop_change) / len(pop_change)

    top_change = max(pop_change)
    low_change = min(pop_change)

    top_year = pop_change.index(top_change)
    low_year = pop_change.index(low_change)

    t_year = years[top_year]
    l_year = years[low_year]

    return avg_change, top_change, low_change, t_year, l_year


    
def main():
    population = pop_list()
    years = year()
    pop_change = change(population)
    avg_change, top_change, low_change, t_year, l_year = calculations(pop_change, years)

    print("The average change was", format(avg_change, sep=''))
    print("The highest change was", top_change, "in the year", t_year)
    print("The lowest change was", low_change, "in the year", l_year)

main()

        

    



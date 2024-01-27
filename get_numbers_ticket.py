import random
def get_numbers_ticket(min, max, quantity):
    population = []
    try:
        if min >= 1 and max < 1001 and quantity <= (max-min):
            for i in range(min,max):
                population.append(i)
            return sorted(random.sample(population, quantity))
        else:
            return ['Error']
    except ValueError:
            return ['Error']

        

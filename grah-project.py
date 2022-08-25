'''

This program calculate in how many years the Country A, surpass or equalize your population, with Contry B.

And, show a graphic that inform the growth of the two Contries.



'''
from cProfile import label
import matplotlib.pyplot as plt


pop_a = int(input('Type the number of all population that inhabits in the Country A: '))
pop_b = int(input('Type the number of all population that inhabits in the Country B: '))

pop_a_to_grahp = pop_a
pop_b_to_grahp = pop_b

if pop_a_to_grahp >= pop_b_to_grahp:
    print('\nA população do pais A não pode ser maior que a do pais B\nThe population of country A cannot be greater than that of country B.\n')
    
else:
    
    tax_a = float(input('Type the percentage of growth of the Country A (50% -- 1.50): '))
    tax_b = float(input('Type the percentage of growth of the Country B (30% -- 1.30): '))
    
    if tax_a <= tax_b:
        print('\nA Taxa de crescimento anual do pais A não pode ser menor que a do pais B\nThe annual growth rate of country A cannot be smaller than that of country B\n')
        
    else:
        calc_years = 0

        pop_a_graphic = []
        pop_b_graphic = []
        calc_years_graphic = []

        while True: 
            pop_a_to_grahp *= tax_a   
            pop_a_graphic.append(pop_a_to_grahp) # exit of pop_a with INT
            
            pop_b_to_grahp *= tax_b
            pop_b_graphic.append(pop_b_to_grahp) 
        
            calc_years += 1   
            calc_years_graphic.append(calc_years)
            
            
            if pop_a_to_grahp >= pop_b_to_grahp:
                print(f'The country A, with a rate of growth of {tax_a}, it took {calc_years} years, to equalize or to surpass the population of Country B')
                
                
                plt.rcParams["figure.autolayout"] = True
                plt.figure(1, figsize=(7,3))
                overlapping = 0.150
                
                plt.plot(calc_years_graphic, pop_a_graphic, color= 'blue')
                plt.plot(calc_years_graphic, pop_b_graphic, color='red')
                plt.axis([1, calc_years, 0, max(pop_a_graphic) + 600])
            # plt.axis('auto')
                plt.title('Graph of the growth of two Countries (A, B)')
                plt.suptitle(f'The population initial of the Country A  is [{pop_a}] and The population initial of the Country B is [{pop_b}]\n with  growth rate of [{tax_a}] - Country A,  and  [{tax_b}] - Country B', fontsize = 8, color = 'blue')
                plt.legend(['Population of Country A', 'Population of Country B'], fontsize= 8, loc = 'upper left')
                plt.xlabel('Number of Years')
                plt.ylabel('Number of Population')

                plt.show()
                break
import pandas as pd
'''
Using Countries_data.csv from Data folder to analyse the data
'''

#first convert the whole file into a DataFrame
world_df = pd.read_csv('E:/python/Data/parsed_country_data.csv')
#print(world_df)

number_of_countries = world_df.shape[0] - 1
#First, lets find the total population of all the countries
world_population = sum(world_df['Population'])
print("The population of the world is: ", world_population)

'''
We know that the shape member variable of the data frame returns a tuple containing the dimensions of the dataframe.
SO we can use the number of columns to find the number of countries
'''

avg_world_population = world_population/number_of_countries
print("The average population of all the countries is: ", int(avg_world_population))


avg_population_density = world_df['Pop. Density'].sum()/number_of_countries
print(f"The average population densities of all the countries is: {avg_population_density} ")


avg_per_capita = world_df['GDP'].sum()/number_of_countries
print("The average per capita income of all the countries is: ", float(avg_per_capita), "$")


avg_inf_mort = world_df['Infant mortality'].sum()/number_of_countries
print("The average infant mortality rate of all the countries is: ",float(avg_inf_mort))


#Lets find the number of high, low and middle income countries
middle_income_countries = 0
upper_middle_income_countries = 0
high_income_countries = 0
low_income_countries = 0

for gdp_pc in world_df['GDP']:
    if gdp_pc > 13205:
        high_income_countries += 1
    elif 4256 < gdp_pc < 13205:
        upper_middle_income_countries += 1
    elif 1086 < gdp_pc < 4256:
        middle_income_countries += 1
    else:
        low_income_countries += 1

print("The number of Low income countries are: ", low_income_countries)
print("The number of middle incoem countries are: ", middle_income_countries)
print("The number of upper middle income countries are: ", upper_middle_income_countries)
print("The number of high income countries are: ", high_income_countries)

#Let's asses the effect of population denstiy on GDP per capita
iter = 0
avg_pop_dens_income_wise = [0, 0, 0, 0]
while iter < 227:
    if world_df['GDP'][iter] > 13205:
        avg_pop_dens_income_wise[3] += world_df['Pop. Density'][iter]
    elif 4256 < world_df['GDP'][iter] < 13205:
        avg_pop_dens_income_wise[2] += world_df['Pop. Density'][iter]
    elif 1086 < world_df['GDP'][iter] < 4256:
        avg_pop_dens_income_wise[1] += world_df['Pop. Density'][iter]
    else:
        avg_pop_dens_income_wise[0] += world_df['Pop. Density'][iter]
    iter += 1

print("The average population density of low income countries is: ", (avg_pop_dens_income_wise[0]/low_income_countries))
print("The average population density of middle income countries is ", (avg_pop_dens_income_wise[1]/middle_income_countries))
print("The average population density of upper middle income countries is ", avg_pop_dens_income_wise[2]/upper_middle_income_countries)
print("The average population density of rich countries is ", avg_pop_dens_income_wise[3]/high_income_countries)

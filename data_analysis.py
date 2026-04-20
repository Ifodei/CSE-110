year_input = int (input ("Enter your year of interest\n"))
lowest_life_expectancy_so_far = 999999999
highest_life_expectancy_so_far = -1
country_with_lowest_life_expectancy = ""
country_with_highest_life_expectancy = ""
year_with_lowest_life_expectancy = 0
year_with_highest_life_expectancy = 0
average = 0
counter = 0 
life_expectancy_total = 0
min_life_expectancy = 9999999999999
max_life_expectancy = -1


with open ( "life-expectancy.csv") as data_list:
    next(data_list)

    for items in data_list:
        items = items.strip()
        parts = items.split(",")
        entity = parts [0]
        code = parts [1]
        year = int (parts [2])
        life_expectancy = float (parts [3])

        if life_expectancy < lowest_life_expectancy_so_far:
            lowest_life_expectancy_so_far = life_expectancy
            country_with_lowest_life_expectancy = entity
            year_with_lowest_life_expectancy = year

        if life_expectancy > highest_life_expectancy_so_far:
            highest_life_expectancy_so_far = life_expectancy
            country_with_highest_life_expectancy = entity
            year_with_highest_life_expectancy = year

        if year_input == year:
            year = year_input
            #it counts for the year the user input in the entire list:
            counter +=1
            #This sums the total life expectancy corresponding to the year inputted by user:
            life_expectancy_total += life_expectancy
            average = life_expectancy_total/counter
            if life_expectancy < min_life_expectancy:
                min_life_expectancy = life_expectancy
                country_one = entity
            if life_expectancy > max_life_expectancy:
                max_life_expectancy = life_expectancy
                country_two = entity


print (f"The year with lowest life expectancy is {year_with_lowest_life_expectancy} from {country_with_lowest_life_expectancy}")
print (f"The year with highest life expectancy is {year_with_highest_life_expectancy} from {country_with_highest_life_expectancy}")
print (f"For the year {year_input}:\n The average life expectancy across all countries was {average:.2f}\n The max life expectancy was in {country_two} with {max_life_expectancy:.2f}\n The min life expectancy was in {country_one} with {min_life_expectancy:.2f}")
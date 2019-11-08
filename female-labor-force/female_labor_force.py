import csv

from pygal_maps_world.maps import World

from country_codes import get_country_code

# Load the data.
filename = 'data/female_labor_force.csv'
with open(filename) as f:
    reader = csv.reader(f)

    # Find the header row.
    for i, row in enumerate(reader):
        if i == 4:
            header_row = row

            # Create the dictionary containing country code and percentage of women
            # in labor force.
            cc_pop = {}
            for row in reader:
                # Eliminate the empty rows.
                if row:
                    # Find population in 2016.
                    population = row[61]
                    # Eliminate empty values.
                    if population != '':
                        population = int(float(population))
                        country_name = row[0]
                        country_code = get_country_code(country_name)
                        if country_code:
                            cc_pop[country_code] = population

            # Group the countries into 3 percentage levels.
            cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
            for cc, pop in cc_pop.items():
                if pop < 30:
                    cc_pop_1[cc] = pop
                elif pop < 45:
                    cc_pop_2[cc] = pop
                else:
                    cc_pop_3[cc] = pop

            # See how many countries are in each group.
            print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))


            # Create the map.
            wm = World()
            wm.title = 'Female Labor Force in 2016, %'
            wm.add('<30%', cc_pop_1)
            wm.add('30-45%', cc_pop_2)
            wm.add('>45%', cc_pop_3)

            wm.render_to_file('female_labor_force.svg')




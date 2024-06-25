import pandas as pd
drinks = pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/drinks.csv',
                   sep=',',
                   index_col='country')

# worldwide average beer_servings counts
print(drinks.beer_servings.mean())

# average beer_servings counts of every continents
print(drinks.groupby('continent').beer_servings.mean())

# wine_servings : max, min, mean on every continents
print(drinks.groupby('continent').wine_servings.agg(['min','max','mean']))

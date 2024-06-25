import pandas as pd
chipo = pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/chipotle.tsv',
                   sep='\t')

# change item_price type from str to float
price = [float(value[1:]) for value in chipo.item_price]
chipo.item_price = price

# calculate average item_price
print(round(chipo.item_price.mean()))

# find the data which its item_price is over 7
print(chipo[chipo.item_price > 7])

# find the item_price over 10 and choice_description contains 'Fresh Tomato Salsa'
print(chipo[(chipo.item_price > 10) & (chipo.choice_description.str.contains('Fresh Tomato Salsa'))])

# find the most expensive data price
print(chipo.sort_values('item_price', ascending=False).head(1))

# use iloc to slice row3 to row10 and column-order_id to column-item_name 
print(chipo.iloc[3:11, 0:3])

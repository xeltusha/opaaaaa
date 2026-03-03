import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Housing.csv")
df.head()

df['date'] = pd.to_datetime(df['date'])
df['price'] = (df['price']/1000 ).round(2)

avg_price_by_zip = df.groupby('zipcode')['price'].mean()

plt.figure(figsize=(12, 8))

bars = plt.bar(avg_price_by_zip.index.astype(str), avg_price_by_zip.values, color='lightblue', edgecolor='black')

plt.xlabel('Zipcode', fontsize=12)
plt.ylabel('Average Price (in Thousands)', fontsize=12)
plt.title('Average Price by Zipcode', fontsize=15)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

avg_price_by_bedrooms = df.groupby('bedrooms')['price'].mean()

plt.figure(figsize=(10, 6))

bars = plt.bar(avg_price_by_bedrooms.index, avg_price_by_bedrooms.values, color='skyblue', edgecolor='black')

plt.xlabel('Number of Bedrooms', fontsize=12)
plt.ylabel('Average Price', fontsize=12)
plt.title('Average Price by Number of Bedrooms', fontsize=15)
plt.tight_layout()
plt.show()

avg_price_by_waterfront = df.groupby('waterfront')['price'].mean()
plt.bar(avg_price_by_waterfront.index,avg_price_by_waterfront.values)
plt.ylabel('avg price in thouands')
plt.xlabel('WaterFront')
plt.xticks([0, 1], ['No Waterfront', 'Waterfront'])
plt.show()

plt.scatter(df['sqft_living'], df['price'])
plt.title('living area vs. price')
plt.xlabel('living area (sqft)')
plt.ylabel('price')
plt.show()

avg_price_by_condition = df.groupby('condition')['price'].mean()
plt.bar(avg_price_by_condition.index,avg_price_by_condition.values)
plt.title('condition vs. avgprice')
plt.xlabel('condition')
plt.ylabel('price')
plt.xticks([1,2,3,4,5],['verybad','bad','normal','good','verygood'])
plt.show()

avg_price_by_ybuilt = df.groupby('yr_built')['price'].mean()

plt.figure(figsize=(10, 6))
plt.plot(avg_price_by_ybuilt.index, avg_price_by_ybuilt.values, color='b', linestyle='-', linewidth=2)
plt.xlabel('Year Built', fontsize=12)
plt.ylabel('Average Price', fontsize=12)
plt.title('Average Price by Year Built', fontsize=15)
plt.tight_layout()
plt.show()

df['with_basement'] = df['sqft_basement'].apply(lambda x: 1 if x > 0 else 0)
avg_price_by_basement = df.groupby('with_basement')['price'].mean()

plt.figure(figsize=(10, 6))

bars = plt.bar(avg_price_by_basement.index, avg_price_by_basement.values, color=['red', 'green'], edgecolor='black')

plt.xticks([0, 1], ['Without Basement', 'With Basement'])
plt.xlabel('Basement Presence', fontsize=12)
plt.ylabel('Average Price', fontsize=12)
plt.title('Average Price Comparison by Basement Presence', fontsize=15)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
plt.scatter(df['sqft_lot15'], df['price'], color='skyblue', s=50, edgecolor='black', alpha=0.7)
plt.xlabel('Lot Size (sqft_lot15)', fontsize=12)
plt.ylabel('Price', fontsize=12)
plt.title(' Price by Lot Size (sqft_lot15)', fontsize=15)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
avg_price_by_lat_long = df.groupby(['lat','long'])['price'].mean()
scatter = plt.scatter(df['lat'], df['long'], c=df['price'], cmap='plasma', s=200, edgecolor='black', linewidth=1.2)

cbar = plt.colorbar(scatter)
cbar.set_label('Price')

plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Scatter plot of Latitude vs Longitude with Price', fontsize=15)
plt.tight_layout()
plt.show()


avgprice_by_floors = df.groupby('floors')['price'].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(avgprice_by_floors['floors'], avgprice_by_floors['price'], color='skyblue', edgecolor='black')
plt.xlabel('Number of Floors', fontsize=12)
plt.ylabel('Average Price', fontsize=12)
plt.title('Average Price by Number of Floors', fontsize=15)
plt.tight_layout() 
plt.show()
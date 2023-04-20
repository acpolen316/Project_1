import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('housing.csv', encoding='utf-8')
df['rooms_per_household'] = df['total_rooms']/df['households']

RPH = df['ocean_proximity'].unique()
for x in RPH:
    df_1 = df.loc[df['ocean_proximity'] == x]
    avg = df_1['rooms_per_household'].mean()
    print(x)
    print(avg)
# rph = {'NEAR BAY':5.222919471393093,'<1H OCEAN':5.153029471295788, 'INLAND':5.98134072288078, 'NEAR OCEAN':5.208174674540822, 'ISLAND':5.65657716330408}

# x_vals = list(rph.keys())
# y_vals = list(rph.values())

# fig, ax = plt.subplots()

# ax.bar(x_vals, y_vals)

# ax.set(xlabel='Ocean Proximity', ylabel='Avg. Rooms / Household',
#        title='Rooms per Household All Regions')

# ax.grid()

# plt.show()

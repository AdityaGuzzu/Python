import pandas as pd
world_df = pd.read_csv('E:/python/Data/parsed_country_data.csv')
region_wise_df = world_df.groupby('Region')[['Population', 'Coastline', 'GDP', 'Area']].mean()
region_wise_df.plot()


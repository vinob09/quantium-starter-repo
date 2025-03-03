import pandas as pd
import glob

# df = pd.read_csv('./daily_sales_data_0.csv')
# print(df)

# filter by product name
target_product = 'pink morsel'
# create list of all csv files
csv_files = ['./daily_sales_data_0.csv', './daily_sales_data_1.csv', './daily_sales_data_2.csv']
# initialize empty list to store dataframes
filtered_data = []
# loop through each file
for file in csv_files:
    # read csv file
    df = pd.read_csv(file)
    # filter for specific product
    df_filtered = df[df['product'] == target_product].copy()
    df_filtered['price'] = df_filtered['price'].replace({'\$': ''}, regex=True).astype(float)
    # create new Sales column by price and quantity
    df_filtered['sales'] = df_filtered['price'] * df_filtered['quantity']
    # print(df_filtered.columns.tolist)
    # keep only required columns
    required_cols = {'sales', 'date', 'region'}
    df_filtered = df_filtered[list(required_cols.intersection(df_filtered.columns))]
    print(df_filtered)
    # append data to list
    filtered_data.append(df_filtered)
# combine all filtered data into one dataframe
final_df = pd.concat(filtered_data, ignore_index=True)
# save to new csv file
final_df.to_csv('filtered_output.csv', index=False)

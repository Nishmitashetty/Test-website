import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(r'C:\Users\10645863\Desktop\Python Programs\sales.xlsx')
print(df.head())
print(df.columns)
print(df.tail())
sales_data = df.groupby('Order Date')[['Sales', 'Profit']].sum()
print(sales_data.sort_values(by = ['Profit']))
plt.scatter(sales_data['Profit'], sales_data['Sales'])
plt.show()
                                   

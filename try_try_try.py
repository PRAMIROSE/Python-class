import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('C://Users//dell//Desktop//learning_python//try_try_try.xlsx')

# Create the plot with lines and markers
plt.plot(df['a'], 
         df['b'], 
         marker='o', linestyle='--', label='Horizontal Visibility', color='blue')


plt.title('Relationship with Air Temperature')
plt.xlabel('Air Temperature 1 Hour Average')
plt.ylabel('Values')
plt.grid()
plt.legend()
plt.show()

# Debugging information
print(df.head())  # Check first few rows
print(df.columns)  # Verify column names
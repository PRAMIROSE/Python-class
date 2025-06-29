import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('C://Users//dell/Desktop//learning_python//AnalysisData.xlsx')
#df.plot(x="Air Temperature 1 Hour Average",y=["Horizontal Visibility 10 min inst","Relative Humidity 1 hour average",
# "Wind direction (deg) at 10 m, 1 h avg"],kind="line")

plt.plot(df['Time'], df['Horizontal Visibility 10 min inst'], marker='o',label='B',color='blue')
plt.plot(df['Air Temperature 1 Hour Average'], df['Relative Humidity 1 hour average'], marker='s', label='C',color='orange')
plt.plot(df['Air Temperature 1 Hour Average'], df['Wind direction (deg) at 10 m, 1 h avg'], marker='^', label='D',color='green')

plt.title('Line Graph')
plt.xlabel('A')
plt.ylabel('Values of B, C, D')
plt.grid()
plt.show()
print(df.head())  # Check first few rows
print(df.columns)  # Verify column names

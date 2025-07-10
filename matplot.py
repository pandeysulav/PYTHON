# import matplotlib.pyplot as plt
# data = [12,15,17,23,27,29,34,36,46]
# plt.plot(data)
# plt.xlabel('indexing')
# plt.ylabel('value')
# plt.title('LINE CHART')
# plt.show()

# CODE 2
# Multiple Chart
# import_goods = [0.96,0.84,0.76,0.78,0.67,0.98,0.67,0.74]
# export_goods = [0.04,0.32,0.67,0.23,0.90,0.12,0.72,0.74]
# years = range(2014,2024)  #2024 exclude
# plt.plot (years, import_goods,marker = 'o')
# plt.plot (years, export_goods, marker = 'x')
# plt.title("IMPORT AND EXPORT RATE")
# plt.xlabel("YEARS")
# plt.ylabel("VALUE")
# plt.show()

# #code3: BAR GRAPH

# years = [1990, 2000, 2010, 2020, 2030]
# growth = [0.1, 0.5, 0.3, 0.2, 0.8]
# plt.bar(years,growth)
# plt.xlabel('Years')
# plt.ylabel('Growth percentage')
# plt.title("BAR GRAPH")
# plt.show()


# #MULTI BAR GRAPH
# import_goods = [0.96,0.84,0.76,0.63,0.54,0.45,0.34,0.20]
# export_goods = [0.04,0.12,0.22,0.23,0.34,0.65,0.72,0.74]
# years = range(2014,2024)  #2024 exclude
# plt.bar (years, import_goods)
# plt.bar (years, export_goods)
# plt.title("IMPORT AND EXPORT RATE")
# plt.xlabel("YEARS")
# plt.ylabel("VALUE")
# plt.legend('IMPORT GOODS','EXPORT GOODS')
# plt.show()


# x = ['Brazil', 'Italy', 'Germany']
# y = [5,4,4]
# plt.bar(x,y)
# plt.xlabel('Country')
# plt.ylabel('Trophies won in FIFA world cup')
# plt.title('BAR GRAPH')
# plt.show()

# # import seaborn as sb
# # sb.displot([0,1,2,3,4,5,6])
# # plt.show()
# # sb.distplot([0,1,2,3,4,5,6],hist = False)
# # plt.show()

# # READING A CSV FILE (Data.csv updated)
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
data=pd.read_csv(r'C:\Users\A S U S\OneDrive\Documents\OneDrive\Desktop\data.csv',encoding='unicode_escape')
print(data.head(10))
print(data.tail())
print(data.to_string())
print(data.info())
print(data.columns)
# Line plot
plt.plot(data['Calories'],c='yellow')
plt.plot(data['Duration'],c='black')

plt.show()

plt.plot(data['Pulse'])
plt.plot(data['Calories'],c='yellow')
print(data.corr(numeric_only=True))
dataplot=sb.heatmap(data.corr(numeric_only=True),cmap='seismic',annot=True)
plt.show()

plt.scatter(data['Pulse'],data['Calories'],c='red',s=20)
plt.title("Scatter plot")
plt.colorbar()
plt.show()
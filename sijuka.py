import matplotlib.pyplot as plt
years = [1990, 2000, 2010, 2020, 2030]
growth = [0.1, 0.5, 0.3, 0.2, 0.8]
plt.bar(years,growth)
plt.xlabel('Years')
plt.ylabel('Growth percentage')
plt.title("BAR GRAPH")
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create some random data
data = np.random.randn(100)

# Convert to DataFrame
df = pd.DataFrame(data, columns=["values"])

# Display first 5 rows
print("Sample Data:")
print(df.head())

# Plot using matplotlib
plt.figure(figsize=(8, 4))
plt.plot(df["values"])
plt.title("Random Values Line Plot (Matplotlib)")
plt.show()

# Plot using seaborn
sns.histplot(df["values"], kde=True)
plt.title("Random Values Histogram (Seaborn)")
plt.show()

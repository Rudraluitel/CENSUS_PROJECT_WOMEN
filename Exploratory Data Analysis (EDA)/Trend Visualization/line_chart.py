# Use line charts to visualize population and birth trends for each racial group
# (White, Hispanic, Asian, African American) over time.

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:\\Users\\Rudra\\Desktop\\CENSUS_PROJECT_WOMEN\\Data_Final.csv"
data = pd.read_csv(file_path)

# Set the Year as the index for easier plotting
data["Year"] = pd.to_datetime(data["Year"], format="%Y")
data.set_index("Year", inplace=True)

# Plotting the trends
plt.figure(figsize=(14, 8))

# Subplot for Female Population trends
plt.subplot(2, 1, 1)
plt.plot(data.index, data["WFP"], label="White Female Population", marker="o")
plt.plot(data.index, data["HFP"], label="Hispanic Female Population", marker="o")
plt.plot(data.index, data["AFP"], label="Asian Female Population", marker="o")
plt.plot(
    data.index, data["AAFP"], label="African American Female Population", marker="o"
)
plt.title("Female Population Trends by Race (2010-2022)")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend()
plt.grid(True)

# Subplot for Birth trends
plt.subplot(2, 1, 2)
plt.plot(data.index, data["WB"], label="White Births", marker="o")
plt.plot(data.index, data["HB"], label="Hispanic Births", marker="o")
plt.plot(data.index, data["AB"], label="Asian Births", marker="o")
plt.plot(data.index, data["AAB"], label="African American Births", marker="o")
plt.title("Birth Trends by Race (2010-2022)")
plt.xlabel("Year")
plt.ylabel("Births")
plt.legend()
plt.grid(True)

# Adjust layout and show the plots
plt.tight_layout()
plt.show()

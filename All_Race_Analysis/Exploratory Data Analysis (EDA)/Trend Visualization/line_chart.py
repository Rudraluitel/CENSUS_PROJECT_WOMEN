import pandas as pd
import matplotlib.pyplot as plt


file_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\All_Race_Analysis\3_processed_data\processed_data3.csv"
data = pd.read_csv(file_path)


data["Year"] = pd.to_datetime(data["Year"], format="%Y")
data.set_index("Year", inplace=True)


plt.figure(figsize=(14, 8))

plt.subplot(2, 1, 1)
(line1,) = plt.plot(data.index, data["White_Female_Pop"], label="White", marker="o")
(line2,) = plt.plot(
    data.index, data["Hispanic_Female_Pop"], label="Hispanic", marker="o"
)
(line3,) = plt.plot(data.index, data["Asian_Female_Pop"], label="Asian", marker="o")
(line4,) = plt.plot(
    data.index,
    data["African_American_Female_Pop"],
    label="African American",
    marker="o",
)
(line5,) = plt.plot(data.index, data["Other_Total_Pop"], label="Other", marker="o")
plt.title("Female Population Trends by Race (2010-2022)")
plt.xlabel("Year")
plt.ylabel("Population")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(data.index, data["White_Births"], marker="o")
plt.plot(data.index, data["Hispanic_Births"], marker="o")
plt.plot(data.index, data["Asian_Births"], marker="o")
plt.plot(data.index, data["African_American_Births"], marker="o")
plt.plot(data.index, data["Other_Total_Births"], marker="o")
plt.title("Birth Trends by Race (2010-2022)")
plt.xlabel("Year")
plt.ylabel("Births")
plt.grid(True)

lines = [line1, line2, line3, line4, line5]
labels = [line.get_label() for line in lines]

plt.legend(lines, labels, loc="upper right")
plt.tight_layout()
plt.show()

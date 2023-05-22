import pandas as pd
import matplotlib.pyplot as plt


ACRES_PER_HECTARE = 2.471
totals = {}


# "In 1981, wildfires in Alberta burned 1,357,305 hectares." (3,353,900 acres)
# https://globalnews.ca/news/5661406/alberta-wildfire-season-hectares-burned-record-1981/
def one():
    csvFile = r"opendata/af-historic-wildfires-1961-1982-data.csv"
    df = pd.read_csv(csvFile, usecols=["YEAR", "TOTAL", "FIRENUMBER"])
    for year in range(61, 82 + 1):
        dfYear = df[df["YEAR"] == year]
        sum = dfYear["TOTAL"].sum()
        # print(f"19{year}\t{int(sum)}")
        totals[1900 + year] = int(sum)


def two():
    csvFile = r"opendata/af-historic-wildfires-1983-1995-data.csv"
    df = pd.read_csv(csvFile, usecols=["fire_year", "extingsize", "firenumber"])
    for year in range(1983, 1995 + 1):
        dfYear = df[df["fire_year"] == year]
        sum = dfYear["extingsize"].sum() * ACRES_PER_HECTARE
        # print(f"{year}\t{int(sum)}")
        totals[year] = int(sum)


# THIS ONE HAS PROBLEMS IN THE DATA DICTIONARY
def three():
    csvFile = r"opendata/af-historic-wildfires-1996-2005-data.csv"
    df = pd.read_csv(csvFile, usecols=["fire_year", "current_size", "fire_number"])
    years = range(1996, 2005 + 1)
    for year in years:
        dfYear = df[df["fire_year"] == year]
        sum = dfYear["current_size"].sum() * ACRES_PER_HECTARE
        # print(f"{year}\t{int(sum)}")
        totals[year] = int(sum)


def four():
    csvFile = r"opendata/af-historic-wildfires-2006-2018-data.csv"
    df = pd.read_csv(
        csvFile,
        usecols=["fire_year", "current_size", "fire_number"],
        encoding="cp1252",
    )
    years = range(2006, 2018 + 1)
    for year in years:
        dfYear = df[df["fire_year"] == year]
        sum = dfYear["current_size"].sum() * ACRES_PER_HECTARE
        # print(f"{year}\t{int(sum)}")
        totals[year] = int(sum)


one()
two()
three()
four()

#  https://en.wikipedia.org/wiki/2019_Alberta_wildfires
totals[2019] = 1985228

# https://globalnews.ca/news/7396849/alberta-2020-slow-wildfire-season/
totals[2020] = 3265 * ACRES_PER_HECTARE

# https://globalnews.ca/news/8343587/alberta-wildfire-season-2021-wraps-up/
totals[2021] = 52955 * ACRES_PER_HECTARE

# https://globalnews.ca/news/9251162/alberta-wildfire-season-dry-conditions/
totals[2022] = 153124 * ACRES_PER_HECTARE

# https://en.wikipedia.org/wiki/2023_Alberta_wildfires
totals[2023] = 842000 * ACRES_PER_HECTARE


totalsDF = pd.DataFrame.from_dict(totals, orient="index", columns=["Acres"])

print(totalsDF)

chart = totalsDF.plot.bar()
plt.savefig("AB wildfires 1961-2023.pdf")
plt.savefig("AB wildfires 1961-2023.png")

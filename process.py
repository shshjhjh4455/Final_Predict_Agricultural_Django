import pandas as pd
import sqlite3

# Read csv file.
df = pd.read_csv("rawdata/weather_2021_2022.csv")
df.columns = ["year", "location", "month", "avr", "max", "min", "rain", "sun"]

# Connect to (create) database.
database = "db.sqlite3"
conn = sqlite3.connect(database)
dtype = {
    "연도": "IntegerField",
    "지역": "CharField",
    "월": "IntegerField",
    "평균기온(°C)": "FloatField",
    "최고기온(°C)": "FloatField",
    "최저기온(°C)": "FloatField",
    "월합강수량(00~24h만)(mm)": "FloatField",
    "합계 일사량(MJ/m2)": "FloatField",
}
df.to_sql(
    name="save_csv_baechoo_new",
    con=conn,
    if_exists="append",
    index=True,
    index_label="id",
)  # dataframe을 sqlite로 저장
conn.close()

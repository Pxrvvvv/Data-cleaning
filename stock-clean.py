import pandas as pd
import numpy as np

df =pd.read_csv("top_1500_stock.xls")
print(df.head(10))

print(df.info())
print(df.shape)
print(df.isnull().sum())

specific_missing_value_column = df.loc[:, df.isna().any()].dtypes
print(specific_missing_value_column)


# cleaning the price_to_earn column
print(df["price_to_earn"].isnull().sum())

print(df["price_to_earn"].head(20))

df["price_to_earn"] = df["price_to_earn"].fillna(np.median(df["price_to_earn"].dropna())) 
print(df["price_to_earn"])

print(df["price_to_earn"].isnull().sum())

# cleaning the dividend_yield(%) column

print(df["dividend_yield(%)"].info())
print(df["dividend_yield(%)"].isnull().sum())

print(df["dividend_yield(%)"].head(20))

print(df["dividend_yield(%)"].max())
print(df["dividend_yield(%)"].min())

df["dividend_yield(%)"] = df["dividend_yield(%)"].fillna(np.mean(df["dividend_yield(%)"]))
print(df["dividend_yield(%)"])

print(df["dividend_yield(%)"].isnull().sum())

# cleaning the YOY_Quarterly_profit_growth(%) column

print(df["YOY_Quarterly_profit_growth(%)"].info())

print(df["YOY_Quarterly_profit_growth(%)"].isnull().sum())

print(df["YOY_Quarterly_profit_growth(%)"].head(20))
print(df["YOY_Quarterly_profit_growth(%)"].max())
print(df["YOY_Quarterly_profit_growth(%)"].min())

df["YOY_Quarterly_profit_growth(%)"] = df["YOY_Quarterly_profit_growth(%)"].fillna(np.median(df['YOY_Quarterly_profit_growth(%)'].dropna()))

print(df["YOY_Quarterly_profit_growth(%)"])

print(df["YOY_Quarterly_profit_growth(%)"].isnull().sum())


# cleaning YOY_Quarterly_sales_growth(%) column 

print(df["YOY_Quarterly_sales_growth(%)"].head(20))
print(df["YOY_Quarterly_sales_growth(%)"].max())
print(df["YOY_Quarterly_sales_growth(%)"].min())

df["YOY_Quarterly_sales_growth(%)"] = df["YOY_Quarterly_sales_growth(%)"].fillna(np.mean(df["YOY_Quarterly_sales_growth(%)"]))

print(df["YOY_Quarterly_sales_growth(%)"])

print(df["YOY_Quarterly_sales_growth(%)"].isnull().sum())

# cleaning Return_on_capital_employed(%) column

print(df["Return_on_capital_employed(%)"].head(20))
print(df["Return_on_capital_employed(%)"].max())
print(df["Return_on_capital_employed(%)"].min())

df["Return_on_capital_employed(%)"] = df["Return_on_capital_employed(%)"].fillna(np.mean(df["Return_on_capital_employed(%)"]))

print(df["Return_on_capital_employed(%)"])

print(df["Return_on_capital_employed(%)"].isnull().sum())

print(df.isnull().sum())

saving_file = df.to_csv("cleaned_stock_data.csv", index=False)
print(saving_file)
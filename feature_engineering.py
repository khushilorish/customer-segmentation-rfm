import pandas as pd

def create_rfm_features(x):
    # create TotalPrice feature
    x["TotalPrice"] = x["Quantity"] * x["Price"]


    # Reference date
    reference_date = x["InvoiceDate"].max() + pd.Timedelta(days=1)
    recency = (x.groupby("Customer ID")["InvoiceDate"].max().reset_index())

    recency["Recency"] = (reference_date - recency["InvoiceDate"]).dt.days
    recency=recency.drop(columns=["InvoiceDate"])


    # Frequency 
    frequency = (x.groupby("Customer ID")["Invoice"].nunique().reset_index())
    frequency.rename(columns={"Invoice":"Frequency"}, inplace= True)


    # Monetary
    monetary = x.groupby("Customer ID")["TotalPrice"].sum().reset_index()
    monetary.rename(columns={"TotalPrice": "Monetary"}, inplace=True)

    # Merge
    rfm = recency.merge(frequency, on="Customer ID")
    rfm=rfm.merge(monetary,on="Customer ID")

    return rfm
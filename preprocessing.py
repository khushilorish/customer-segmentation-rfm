from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

def clean_data(x):
    # remove mssing column ID's rows
    x = x.dropna(subset=["Customer ID"])

    # remove description
    x = x.drop(columns=["Description"])

    # remove cancelled transaction
    x = x[~x["Invoice"].str.startswith("C", na=False)]

    # remove invalid transactions
    x = x[~((x["Quantity"] < 0) & (~x["Invoice"].str.startswith("C", na= False)))]

    # remove duplicates
    x = x.drop_duplicates().reset_index(drop=True)

    # remove negative price records
    x = x[~(x["Price"] <0)]

    #  convert invoiceDate into datetime dataType
    x["InvoiceDate"] = pd.to_datetime(x["InvoiceDate"])

    return x


# preprocess rfm data
def preprocess_data(x):

    x[["Recency", "Frequency", "Monetary"]] = np.log1p(x[["Recency", "Frequency", "Monetary"]])

    scaler = StandardScaler()

    rfm_scaled = scaler.fit_transform(x[["Recency", "Frequency", "Monetary"]])

    return rfm_scaled
import pandas as pd

# Simulate loading data
df_transactions = pd.read_csv("data/transactions.csv")
df_profiles = pd.read_csv("data/profiles.csv")

# Merge and clean data
df = pd.merge(df_profiles, df_transactions, on="customer_id", how="left")
df.fillna(0, inplace=True)

# Feature engineering
df["total_spend"] = df["num_transactions"] * df["avg_transaction_value"]

# Save unified data
df.to_csv("data/customer_360.csv", index=False)
print("Customer 360 dataset created.")

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5433/ny_taxi"
)

ds = pd.read_csv("taxi_zone_lookup.csv")

# ds = pd.read_parquet("green_tripdata_2025-11.parquet")

ds.to_sql(
    name="taxi_zones",
    con=engine,
    schema="public",      # default schema in Postgres
    if_exists="replace",  # "append" in real pipelines
    index=False,
    method="multi",       # faster inserts
    chunksize=1000
)

# print(ds.info())
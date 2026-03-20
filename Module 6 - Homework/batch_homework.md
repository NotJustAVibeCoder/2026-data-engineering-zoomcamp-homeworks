# Question 1: Install Spark and PySpark


```python
import pyspark
```


```python
# !wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-11.parquet
```

    --2026-03-20 16:50:58--  https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-11.parquet
    Resolving d37ci6vzurychx.cloudfront.net (d37ci6vzurychx.cloudfront.net)... 3.170.186.111, 3.170.186.229, 3.170.186.198, ...
    Connecting to d37ci6vzurychx.cloudfront.net (d37ci6vzurychx.cloudfront.net)|3.170.186.111|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 71134255 (68M) [binary/octet-stream]
    Saving to: ‘yellow_tripdata_2025-11.parquet’
    
    yellow_tripdata_202 100%[===================>]  67.84M  95.9MB/s    in 0.7s    
    
    2026-03-20 16:50:59 (95.9 MB/s) - ‘yellow_tripdata_2025-11.parquet’ saved [71134255/71134255]
    



```python
from pyspark.sql import SparkSession
spark = (
    SparkSession.builder
    .appName("MyDataPlatform")  # name your job
    .master("local[*]")  # use all cores (good for local dev)
    
    # Core configs
    .config("spark.driver.memory", "4g")
    .config("spark.executor.memory", "4g")
    .config("spark.sql.shuffle.partitions", "200")
    
    # Performance tuning
    .config("spark.sql.execution.arrow.pyspark.enabled", "true")  # faster Pandas conversion
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    
    # Parquet / file handling
    .config("spark.sql.parquet.filterPushdown", "true")
    .config("spark.sql.parquet.mergeSchema", "false")
    
    # Timezone consistency
    .config("spark.sql.session.timeZone", "UTC")
    
    # Optional: enable Hive support if needed
    # .enableHiveSupport()
    
    .getOrCreate()
)
```

    Setting default log level to "WARN".
    To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
    26/03/20 16:53:12 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable


What's the output?
Answer: 3.5.8


```python
spark.version
```




    '3.5.8'



# Question 2: Yellow November 2025


```python
df = spark.read.parquet("yellow_tripdata_2025-11.parquet")
df.repartition(4).write.parquet("yellow_tripdata/2025/11")
```

                                                                                    


```python
!ls -lh yellow_tripdata/2025/11
```

    total 102M
    -rw-r--r-- 1 artemijskurtenoks artemijskurtenoks   0 Mar 20 16:58 _SUCCESS
    -rw-r--r-- 1 artemijskurtenoks artemijskurtenoks 26M Mar 20 16:58 part-00000-88e46eef-20a3-46c5-acfc-7bade3b4240e-c000.snappy.parquet
    -rw-r--r-- 1 artemijskurtenoks artemijskurtenoks 26M Mar 20 16:58 part-00001-88e46eef-20a3-46c5-acfc-7bade3b4240e-c000.snappy.parquet
    -rw-r--r-- 1 artemijskurtenoks artemijskurtenoks 26M Mar 20 16:58 part-00002-88e46eef-20a3-46c5-acfc-7bade3b4240e-c000.snappy.parquet
    -rw-r--r-- 1 artemijskurtenoks artemijskurtenoks 26M Mar 20 16:58 part-00003-88e46eef-20a3-46c5-acfc-7bade3b4240e-c000.snappy.parquet


What is the average size of the Parquet (ending with .parquet extension) Files that were created (in MB)? Select the answer which most closely matches.

Answer: 25MB

# Question 3: Count records

How many taxi trips were there on the 15th of November?

Answer: 162,604


```python
from pyspark.sql import functions as F
```


```python
df = spark.read.parquet("yellow_tripdata/2025/11")
```


```python
df.printSchema()
```

    root
     |-- VendorID: integer (nullable = true)
     |-- tpep_pickup_datetime: timestamp_ntz (nullable = true)
     |-- tpep_dropoff_datetime: timestamp_ntz (nullable = true)
     |-- passenger_count: long (nullable = true)
     |-- trip_distance: double (nullable = true)
     |-- RatecodeID: long (nullable = true)
     |-- store_and_fwd_flag: string (nullable = true)
     |-- PULocationID: integer (nullable = true)
     |-- DOLocationID: integer (nullable = true)
     |-- payment_type: long (nullable = true)
     |-- fare_amount: double (nullable = true)
     |-- extra: double (nullable = true)
     |-- mta_tax: double (nullable = true)
     |-- tip_amount: double (nullable = true)
     |-- tolls_amount: double (nullable = true)
     |-- improvement_surcharge: double (nullable = true)
     |-- total_amount: double (nullable = true)
     |-- congestion_surcharge: double (nullable = true)
     |-- Airport_fee: double (nullable = true)
     |-- cbd_congestion_fee: double (nullable = true)
    



```python
# df.withColumn("pickup_date", F.to_date(df.tpep_pickup_datetime)).select("tpep_pickup_datetime", "pickup_date").show()
```

    +--------------------+-----------+
    |tpep_pickup_datetime|pickup_date|
    +--------------------+-----------+
    | 2025-11-07 15:04:17| 2025-11-07|
    | 2025-11-12 07:48:41| 2025-11-12|
    | 2025-11-01 15:24:44| 2025-11-01|
    | 2025-11-11 06:14:41| 2025-11-11|
    | 2025-11-03 17:34:26| 2025-11-03|
    | 2025-11-11 21:47:10| 2025-11-11|
    | 2025-11-18 11:47:41| 2025-11-18|
    | 2025-11-07 13:57:39| 2025-11-07|
    | 2025-11-05 21:06:15| 2025-11-05|
    | 2025-11-14 00:41:22| 2025-11-14|
    | 2025-11-06 15:58:17| 2025-11-06|
    | 2025-11-13 11:31:05| 2025-11-13|
    | 2025-11-07 13:22:04| 2025-11-07|
    | 2025-11-07 17:04:38| 2025-11-07|
    | 2025-11-08 09:33:24| 2025-11-08|
    | 2025-11-19 07:57:07| 2025-11-19|
    | 2025-11-05 08:19:05| 2025-11-05|
    | 2025-11-04 13:20:38| 2025-11-04|
    | 2025-11-05 11:42:07| 2025-11-05|
    | 2025-11-07 11:14:32| 2025-11-07|
    +--------------------+-----------+
    only showing top 20 rows
    



```python
df.filter(F.to_date(df.tpep_pickup_datetime) == '2025-11-15').count()
```




    162604



# Question 4: Longest trip

What is the length of the longest trip in the dataset in hours?

Answer: 90.6


```python
trip_duration = df.withColumn("trip_duration", (df.tpep_dropoff_datetime - df.tpep_pickup_datetime).cast("long")/3600).select("tpep_pickup_datetime", "tpep_dropoff_datetime" ,"trip_duration")
trip_duration.orderBy(F.col("trip_duration").desc()).limit(1).show()
```

    [Stage 49:>                                                         (0 + 2) / 2]

    +--------------------+---------------------+-----------------+
    |tpep_pickup_datetime|tpep_dropoff_datetime|    trip_duration|
    +--------------------+---------------------+-----------------+
    | 2025-11-26 20:22:12|  2025-11-30 15:01:00|90.64666666666666|
    +--------------------+---------------------+-----------------+
    


                                                                                    

# Question 5: User Interface

Spark's User Interface which shows the application's dashboard runs on which local port?

Answer: 4040

# Question 6: Least frequent pickup location zone

Answer:

Governor's Island/Ellis Island/Liberty Island
Arden Heights


```python
# !wget https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv
```

    --2026-03-20 17:55:01--  https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv
    Resolving d37ci6vzurychx.cloudfront.net (d37ci6vzurychx.cloudfront.net)... 3.170.186.111, 3.170.186.198, 3.170.186.41, ...
    Connecting to d37ci6vzurychx.cloudfront.net (d37ci6vzurychx.cloudfront.net)|3.170.186.111|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 12331 (12K) [text/csv]
    Saving to: ‘taxi_zone_lookup.csv.1’
    
    taxi_zone_lookup.cs 100%[===================>]  12.04K  --.-KB/s    in 0s      
    
    2026-03-20 17:55:01 (96.0 MB/s) - ‘taxi_zone_lookup.csv.1’ saved [12331/12331]
    



```python
zone_lookup = spark.read.csv("taxi_zone_lookup.csv",header=True)
df = spark.read.parquet("yellow_tripdata/2025/11")
```


```python
zone_lookup.createOrReplaceTempView("taxi_zones")
df.createOrReplaceTempView("data")
```


```python
spark.sql("""
    
    select tz.zone, count(*) from data d 
    join taxi_zones tz 
    on d.PULocationID = tz.LocationID
    group by tz.zone
    order by count(*) asc
    
""").show()
```

    [Stage 64:>                                                         (0 + 2) / 2]

    +--------------------+--------+
    |                zone|count(1)|
    +--------------------+--------+
    |Eltingville/Annad...|       1|
    |Governor's Island...|       1|
    |       Arden Heights|       1|
    |       Port Richmond|       3|
    |       Rikers Island|       4|
    |   Rossville/Woodrow|       4|
    |         Great Kills|       4|
    | Green-Wood Cemetery|       4|
    |         Jamaica Bay|       5|
    |         Westerleigh|      12|
    |New Dorp/Midland ...|      14|
    |       West Brighton|      14|
    |             Oakwood|      14|
    |        Crotona Park|      14|
    |       Willets Point|      15|
    |Breezy Point/Fort...|      16|
    |Saint George/New ...|      17|
    |       Broad Channel|      18|
    |     Mariners Harbor|      21|
    |Heartland Village...|      22|
    +--------------------+--------+
    only showing top 20 rows
    


                                                                                    

Answer: 

Governor's Island/Ellis Island/Liberty Island

Arden Heights


```python

```

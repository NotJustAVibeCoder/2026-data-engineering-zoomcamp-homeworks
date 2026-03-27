# Data engineering zoomcamp - Module 7: Streaming. Questions.

# Question 1. Redpanda version

Code:

```bash
docker exec -it module7-homework-redpanda-1 rpk version
```

Answer:
rpk version: v25.3.9

# Question 2. Sending data to Redpanda

```bash
docker exec -it module7-homework-redpanda-1 rpk topic create green-trips
```

# Question 3. Consumer - trip distance

How many trips have trip_distance > 5?

Code (query sink postgres db):

```sql

select count (*) from green_trips where trip_distance > 5

```

Answer:

8506

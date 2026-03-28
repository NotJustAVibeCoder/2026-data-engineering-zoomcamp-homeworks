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

# Part 2: PyFlink (Questions 4-6)

# Question 4. Tumbling window - pickup location

Which PULocationID had the most trips in a single 5-minute window?

Answer 74

# Question 5. Session window - longest streak

How many trips were in the longest session?

Answer: 81

# Question 6. Tumbling window - largest tip

Which hour had the highest total tip amount?

Answer: 2025-10-16 18:00:00

# Project-3-BQuery-Pol-Advertising-Data

## Pick a dataset that interests you (or multiple data sets)

Use the Open Data Sets available from Google BigQuery. You can use your own Google account or Kaggle.

# Imports

# Authentication

# Enable Data Table Entry

# List Projects

Based on the outputs you provided, here are the answers to your questions:

1. How many rows are in the full dataset?

The full dataset contains 1,814,759 rows.

2. How many columns are in the full dataset?

The number of columns varies by table. For example:

- geo_spend has 23 columns

- advertiser_stats has 26 columns

- creative_stats has 56 columns

3. What tables are available in the google_political_ads dataset?

The available tables include:

- geo_spend

- advertiser_stats

- advertiser_weekly_spend

- advertiser_declared_stats

- last_updated

- advertiser_geo_spend

- campaign_targeting

- top_keywords_history

- creative_stats

4. What columns are available in the google_political_ads dataset?

The columns vary by table, but some common columns include:

- advertiser_id

- advertiser_name

- regions

- date_range_start

- date_range_end

- num_of_days

- impressions

- spend_usd

- spend_range_min_usd

- spend_range_max_usd

5. Which advertisers have spent the most money on political ads?

The top advertisers by spending include:

- Biden for President

- Donald J. Trump for President, Inc.

- Mike Bloomberg 2020 Inc.

- Harris Victory Fund

- Trump Make America Great Again Committee

6. How much have specific advertisers (Biden and Trump campaigns) spent on political ads?

The total spending for Biden and Trump campaigns combined is $97,200.

7. What is the total spending of Biden and Trump campaigns combined?

The total spending for Biden and Trump campaigns combined is $97,200.

8. What is the average spending of Biden and Trump campaigns?

The average spending for Biden and Trump campaigns is $1,495.38.

9. How has spending changed over time for a specific advertiser?

The spending trend over time for specific advertisers is not provided in the output, but the query to calculate this is shown.

10. What is the sum of all spending across all advertisers?

The sum of all spending across all advertisers is $1,733,853,600.

11. What is the average spending across all advertisers?

The average spending across all advertisers is $1,237.21.

12. What is the median spending across all advertisers?

The median spending across all advertisers is $100.

13. What are the spending percentiles (1st, 10th, 25th, 50th, 75th, 90th, 99th) across all advertisers?

The spending percentiles are:

- 1st percentile: $100

- 10th percentile: $100

- 25th percentile: $100

- 50th percentile: $100

- 75th percentile: $100

- 90th percentile: $100

- 99th percentile: $900

14. What are the minimum and maximum spending amounts across all advertisers?

The minimum spending amount is $0, and the maximum spending amount is $3,000,000.

15. What are the unique advertiser names in the dataset?

The unique advertiser names are not provided in the output, but the query to find these is shown.

16. What is the maximum spending across all advertisers?

The maximum spending across all advertisers is $3,000,000.

17. How does the spending trend compare between Biden and Trump campaigns over time?

The spending trend comparison between Biden and Trump campaigns over the recent election season has near 0. This shows that more research needs to be done about non Trump and non Biden named advertisers.

### Independant Python Aliases

### Basic Queries

# advstats = advertiser_stats table

# cstats =creative_stats table

#### SELECT (with \* and with column names)

How much has each advertiser spent

#### LIMIT

### AND, FROM, WHERE, GROUP BY,

### AND, LIKE (with % or \_ wildcard)

#### ORDER BY, GROUP BY

#### SUM

#### AVG

#### DISTINCT

### Aggregates

#### MAX

## Make some plots

%%capture

# pandas module

import pandas as pd

import pandas_gbq

import matplotlib.pyplot as plt

# gcp modules

from google.cloud import bigquery

# colab modules

from google.colab import auth

from google.colab import syntax

from google.colab import userdata
auth.authenticate_user()

print('Authenticated')
%load_ext google.colab.data_table

# %unload_ext google.colab.data_table

%alias gcloud gcloud
%%capture

gcloud projects list --sort-by=projectId
project_id = userdata.get('proj-3')
client = bigquery.Client(project=project_id)

THREE_GB = 3 _ 1_000 _ 1_000 _ 1_000 _ 1_000

SIX_GB = 6 _ 1_000 _ 1_000 _ 1_000 _ 1_000

TEN_GB = 10 _ 1_000 _ 1_000 _ 1_000 _ 1_000

row_count = client.query('''

SELECT

    COUNT(1) as total

FROM `bigquery-public-data.google_political_ads.creative_stats`

'''

).to_dataframe()["total"][0]

print(f'Full dataset has {row*count:*} rows')
column_count = client.query('''

SELECT COUNT(column_name) as total

FROM `bigquery-public-data`.google_political_ads.INFORMATION_SCHEMA.COLUMNS

WHERE table_name = 'creative_stats'

''').to_dataframe()["total"][0]

print(f'Full dataset has {column*count:*} columns')

tables = client.query('''

    SELECT table_name

    FROM `bigquery-public-data`.google_political_ads.INFORMATION_SCHEMA.TABLES

''').to_dataframe()

for table in tables['table_name']:

    column_count = client.query(f'''

        SELECT COUNT(column_name) as total

        FROM `bigquery-public-data`.google_political_ads.INFORMATION_SCHEMA.COLUMNS

        WHERE table_name = '{table}'

    ''').to_dataframe()["total"][0]

    print(f'Table {table} has {column_count:_} columns')

schema = client.query('''

SELECT table_name

FROM `bigquery-public-data`.google_political_ads.INFORMATION_SCHEMA.TABLES

''').to_dataframe()

schema

# what are the sum and average of spending by advertisers

advstats = client.query('''

SELECT

    as_.advertiser_id,

    as_.advertiser_name,

    as_.regions,

    SUM(cs.spend_range_min_usd) AS total_spend,

    AVG(cs.spend_range_min_usd) AS avg_spend

FROM

    `bigquery-public-data.google_political_ads.advertiser_stats` AS as_

    INNER JOIN `bigquery-public-data.google_political_ads.creative_stats` AS cs ON as_.advertiser_id = cs.advertiser_id

GROUP BY

    as_.advertiser_id, as_.advertiser_name, as_.regions

ORDER BY total_spend DESC

''').to_dataframe()
advstats

# What data types are the rows in the table?

cstats = client.query('''

SELECT column_name, data_type

FROM `bigquery-public-data`.google_political_ads.INFORMATION_SCHEMA.COLUMNS

WHERE table_name = 'creative_stats'

''').to_dataframe()
cstats

# Select all columns from the advertiser_stats table

all_columns = client.query('''

    SELECT *

    FROM `bigquery-public-data.google_political_ads.advertiser_stats`

    LIMIT 100

''').to_dataframe()

all_columns

# Using LIMIT to show the first 5 rows of the advertiser_stats table

limited_rows = client.query('''

    SELECT *

    FROM `bigquery-public-data.google_political_ads.advertiser_stats`

    LIMIT 5

''').to_dataframe()

limited_rows

# Find the total spending of Biden and Trump campaigns combined.

biden_trump_spending = client.query('''

    SELECT

        SUM(cs.spend_range_max_usd) AS total_spend

    FROM

        `bigquery-public-data.google_political_ads.advertiser_stats` AS as_

        INNER JOIN `bigquery-public-data.google_political_ads.creative_stats` AS cs ON as_.advertiser_id = cs.advertiser_id

    WHERE

        as_.advertiser_name LIKE '%Biden%' OR as_.advertiser_name LIKE '%Trump%'

''').to_dataframe()

biden_trump_spending

# Calculate the average spending of Biden and Trump campaigns.

biden_trump_avg_spending = client.query('''

    SELECT

        AVG(cs.spend_range_max_usd) AS avg_spend

    FROM

        `bigquery-public-data.google_political_ads.advertiser_stats` AS as_

        INNER JOIN `bigquery-public-data.google_political_ads.creative_stats` AS cs ON as_.advertiser_id = cs.advertiser_id

    WHERE

        as_.advertiser_name LIKE '%Biden%' OR as_.advertiser_name LIKE '%Trump%'

''').to_dataframe()

biden_trump_avg_spending
client.query('''

SELECT

    cs1.advertiser_name AS advertiser1,

    cs2.advertiser_name AS advertiser2,

    SUM(cs1.spend_range_min_usd) AS total_spend_1,

    SUM(cs2.spend_range_min_usd) AS total_spend_2

FROM

    `bigquery-public-data.google_political_ads.creative_stats` AS cs1

    INNER JOIN `bigquery-public-data.google_political_ads.creative_stats` AS cs2 ON cs1.advertiser_name != cs2.advertiser_name

WHERE cs1.advertiser_name IN ('BIDEN FOR PRESIDENT', 'HARRIS VICTORY FUND', 'HARRIS FOR PRESIDENT', 'BIDEN VICTORY FUND')

AND cs2.advertiser_name IN ('DONALD J. TRUMP FOR PRESIDENT, INC', 'TRUMP MAKE AMERICA GREAT AGAIN COMMITTEE')

GROUP BY advertiser1, advertiser2

ORDER BY total_spend_1 DESC, total_spend_2 DESC

''').to_dataframe()

# Calculate the sum of 'spend_range_min_usd' for all rows in the 'creative_stats' table.

sum_spend = client.query('''

    SELECT SUM(spend_range_min_usd) AS total_spending

    FROM `bigquery-public-data.google_political_ads.creative_stats`

''').to_dataframe()

sum_spend

# Calculate the average spending across all advertisers.

avg_spending_all = client.query('''

    SELECT AVG(spend_range_max_usd) AS avg_spend

    FROM `bigquery-public-data.google_political_ads.creative_stats`

''').to_dataframe()

avg_spending_all
median_spending = client.query('''

    SELECT APPROX_QUANTILES(spend_range_max_usd, 100)[OFFSET(50)] AS median_spend

    FROM `bigquery-public-data.google_political_ads.creative_stats`

''').to_dataframe()

median_spending
percentile_spending = client.query('''

    SELECT

        PERCENTILE_CONT(spend_range_max_usd, 0.01) OVER() AS percentile_1,

        PERCENTILE_CONT(spend_range_max_usd, 0.10) OVER() AS percentile_10,

        PERCENTILE_CONT(spend_range_max_usd, 0.25) OVER() AS percentile_25,

        PERCENTILE_CONT(spend_range_max_usd, 0.50) OVER() AS percentile_50,

        PERCENTILE_CONT(spend_range_max_usd, 0.75) OVER() AS percentile_75,

        PERCENTILE_CONT(spend_range_max_usd, 0.90) OVER() AS percentile_90,

        PERCENTILE_CONT(spend_range_max_usd, 0.99) OVER() AS percentile_99

    FROM

        `bigquery-public-data.google_political_ads.creative_stats`

    LIMIT 1

''').to_dataframe()

percentile_spending
spend_min_usd = client.query('''

SELECT

MIN(spend_range_min_usd) AS min_spend_min_usd,

MAX(spend_range_min_usd) AS max_spend_min_usd,

AVG(spend_range_min_usd) AS avg_spend_min_usd

FROM `bigquery-public-data.google_political_ads.creative_stats`

''').to_dataframe()

spend_min_usd

# Focus on Top Spenders

for index, row in top_advertisers.iterrows():

    advertiser_id = row['advertiser_id']

    advertiser_name = row['advertiser_name']



    advertiser_spending = client.query(f"""

        SELECT

            t1.date_range_start AS date,

            SUM((t1.spend_range_min_usd + t1.spend_range_max_usd) / 2) / 1000000 AS daily_spend_millions,  # Total spending in millions

            t2.advertiser_name

        FROM

            `bigquery-public-data.google_political_ads.creative_stats` AS t1

        INNER JOIN

            `bigquery-public-data.google_political_ads.advertiser_stats` AS t2

            ON t1.advertiser_id = t2.advertiser_id

        WHERE t1.advertiser_id = '{advertiser_id}'

        AND t1.date_range_start BETWEEN '2023-01-01' AND '2024-12-31'

        GROUP BY

            date, t2.advertiser_name

        ORDER BY

            date

    """).to_dataframe()



    if not advertiser_spending.empty:

        plt.figure(figsize=(10, 6))

        plt.plot(advertiser_spending['date'], advertiser_spending['daily_spend_millions'])  # Plot total spending in millions

        plt.xlabel('Date')

        plt.ylabel('Daily Spending (Millions USD)')

        plt.title(f'Spending Trend for Advertiser: {advertiser_name}')

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt

# Example using DISTINCT to find unique advertiser names

distinct_advertisers = client.query('''

    SELECT DISTINCT advertiser_name

    FROM `bigquery-public-data.google_political_ads.advertiser_stats`

    LIMIT 100

''').to_dataframe()

distinct_advertisers

# Calculate the maximum spending across all advertisers.

max_spending_all = client.query('''

    SELECT MAX(spend_range_max_usd) AS max_spend

    FROM `bigquery-public-data.google_political_ads.creative_stats`

''').to_dataframe()

max_spending_all
biden_spending = client.query('''

SELECT

    cs.date_range_start AS spending_date,

    SUM((cs.spend_range_min_usd + cs.spend_range_max_usd) / 2) AS total_spend

FROM

    `bigquery-public-data.google_political_ads.creative_stats` AS cs

WHERE cs.advertiser_name = 'BIDEN FOR PRESIDENT'

    AND cs.date_range_start BETWEEN '2023-01-01' AND '2024-12-31'  # Filter for 2023-2024

GROUP BY spending_date

ORDER BY spending_date

''').to_dataframe()
biden_spending
adv_name = client.query('''

SELECT DISTINCT advertiser_name

FROM `bigquery-public-data.google_political_ads.creative_stats`

WHERE advertiser_name LIKE '%Trump%'

OR advertiser_name LIKE '%Biden%'

''').to_dataframe()

adv_name
trump_spending = client.query('''

SELECT

    cs.date_range_start AS spending_date,

    SUM((cs.spend_range_min_usd + cs.spend_range_max_usd) / 2) AS total_spend

FROM

    `bigquery-public-data.google_political_ads.creative_stats` AS cs

WHERE cs.advertiser_name IN ('DONALD J. TRUMP FOR PRESIDENT, INC', 'TRUMP MAKE AMERICA GREAT AGAIN COMMITTEE', 'SAVE AMERICA JFC', 'MAKE AMERICA GREAT AGAIN, AGAIN! INC.', 'SAVE AMERICA') # Include more advertiser names

AND cs.date_range_start BETWEEN '2023-01-01' AND '2024-12-31'

GROUP BY spending_date

ORDER BY spending_date

''').to_dataframe()
trump_spending

# Combine the dataframes

spending_over_time = pd.merge(biden_spending, trump_spending, on='spending_date', suffixes=('\_biden', '\_trump'), how='outer') # Use outer join to include all dates

# Convert spending_date to datetime objects

spending_over_time['spending_date'] = pd.to_datetime(spending_over_time['spending_date'])

# Create the plot

plt.figure(figsize=(12, 6))

plt.plot(spending_over_time['spending_date'], spending_over_time['total_spend_biden'], label='Biden')

plt.plot(spending_over_time['spending_date'], spending_over_time['total_spend_trump'], label='Trump')

plt.xlabel('Date')

plt.ylabel('Total Spending (USD)')

plt.title('Biden vs. Trump Campaign Spending Over Time')

plt.legend()

plt.grid(True)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# Project SQL - Chinook

## Chinook data set

See the lecture on SQLite3 using the Chinook data set to set up the software, database, and tables, as well as for the links to ancillary information about the data set.

# Imports

## Come up with questions about your data

Have a look at the Entity-Relation ( ER ) diagram to help come up with questions.

- What sort of information is in this dataset?

- How many records are there?

- How many different countries (states, counties, cities, etc) have records in this data set?

If you are stuck, here are some ideas for questions:

- https://github.com/LucasMcL/15-sql_queries_02-chinook/blob/master/README.md

- [Using the R language](https://rpubs.com/enext777/636199)

- [Search Google](https://www.google.com/search?q=chinook+database+questions)

## Use SQL queries to pull specific information

Do NOT pull all the data and then filter using DataFrame methods etc. Make sure and use AT LEAST 13 of the 15 SQL options listed below. (You may have to get creative and come up with more questions to ask/answer.)

### Basic Queries

#### SELECT (with \* and with column names)

### What data is in this table?

#### WHERE

#### AND

#### OR

#### LIKE (with % or \_ wildcard)

#### BETWEEN

#### LIMIT

### Sorting and Grouping

#### ORDER BY

#### DISTINCT

#### GROUP BY

### Aggregates

#### MAX

#### MIN

#### SUM

#### AVG

#### COUNT

## Make some plots

Make some cool plots to go with your data. Write SQL queries to get ONLY the information you need for each plot. (Don't pull ALL the data and then just plot a few columns.)

## EXTRA CREDIT:

- Use a CTE

- Use a query that joins two or more tables.

- Make a model to see if you can predict something

- Come up with something else cool to do with your data

!apt-get update

!apt-get install -y sqlite3
%%script sqlite3 --column --header chinook.db

PRAGMA table_info(albums);

PRAGMA table_info(artists);

PRAGMA table_info(customers);

PRAGMA table_info(employees);

PRAGMA table_info(genres);

PRAGMA table_info(invoices);

PRAGMA table_info(media_types);

PRAGMA table_info(playlist_track);

PRAGMA table_info(playlists);

PRAGMA table_info(tracks);

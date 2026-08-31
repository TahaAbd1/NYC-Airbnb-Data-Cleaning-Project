# NYC-Airbnb-Data-Cleaning-Project
This project takes the [New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data) 
dataset from Kaggle and cleans it into an analysis-ready format. This is Project #1 in my 
data analysis portfolio, focused on practicing real-world data cleaning: handling missing 
values, fixing data types, removing duplicates, and dealing with outliers.

## Dataset
- **Source:** [Kaggle - New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)
- **Original file:** `AB_NYC_2019.csv`
- **Rows:** ~49,000 listings
- **Columns:** 16 (id, name, host info, location, room type, price, reviews, availability, etc.)

## Issues Found in the Raw Data
- `reviews_per_month` had ~10,000 missing values
- `last_review` had a matching number of missing values (same rows as above)
- `name` and `host_name` had a small number of missing values
- `price` had listings with a value of **0**, which isn't a real rental price
- `price` had extreme outliers (some listings priced in the thousands per night)
- `minimum_nights` had some unrealistically high values (300+ nights)
- Data types needed correcting: `last_review` was stored as text instead of a date

## Cleaning Steps and Reasoning

| Column | Issue | Fix | Why |
|---|---|---|---|
| `reviews_per_month` | Missing values | Filled with `0` | A missing value here means the listing has never been reviewed, not an unknown number — 0 is the honest, factual fill |
| `name`, `host_name` | Missing values | Filled with `'Unknown'` | Dropping these rows would lose otherwise valid price/location data over a cosmetic field |
| `last_review` | Missing values | Left as missing (no fill) | There is no honest placeholder for a date that doesn't exist — inventing one would be misleading |
| `last_review` | Wrong data type (text) | Converted to `datetime` | Enables proper date filtering/sorting for future analysis |
| `neighbourhood_group`, `room_type` | Stored as generic text | Converted to `category` type | These are repeating fixed categories — more memory-efficient and faster to filter |
| All columns | Duplicate rows | Removed with `drop_duplicates()` | Duplicate listings would skew any later counts or averages |
| `price` | Listings priced at $0 | Removed | A $0/night listing is not a real rental — almost certainly a data entry error |
| `price` | Extreme outliers (top 1%) | Removed listings above the 99th percentile | These are likely luxury outliers or data errors that would distort averages; documented as a judgment call rather than a hard rule |
| `minimum_nights` | Some values in the hundreds | Reviewed via `.describe()` | Flagged for awareness; not aggressively filtered so genuine long-term rental listings aren't lost |

## Files in This Repo
- `AB_NYC_2019.csv` — original, untouched raw dataset
- `cleaned_airbnb_nyc.csv` — cleaned output dataset
- `script.py` — notebook with all cleaning steps and code
- `README.md` — this file

## Tools Used
- Python
- pandas
- numpy
- VS Code

## What I'd Do With More Time
- Cross-check `neighbourhood` against `neighbourhood_group` for mismatches (e.g., a neighbourhood listed under the wrong borough)
- Investigate whether `minimum_nights` outliers correlate with specific hosts (possible bulk-listing accounts)
- Geocode/validate `latitude`/`longitude` against NYC borough boundaries to catch mislabeled locations

## Author
[Taha Abdullah] — [TahaAdb1]
Project 1 of a self-directed data analysis learning path (Month 1: Data Cleaning)

### 1. Popularity

This seems to be the most obvious target variable. It's already a float64 type, which is good for regression tasks.

```python
print(df_1['Popularity'].describe())
```

This will give you an overview of the distribution of popularity scores.

### 2. Streams

While this is a measure of past performance, it could potentially be used as a target variable if you're trying to predict future streaming numbers.

```python
print(df_1['Streams'].describe())
```

### 3. Highest Charting Position

This could be a good target if you want to predict how well a song will perform on charts.

```python
print(df_1['Highest Charting Position'].describe())
```

### 4. Number of Times Charted

This could be another good indicator of a song's success.

```python
print(df_1['Number of Times Charted'].describe())
```

### 5. Weeks Charted

This could be a good target if you want to predict how long a song will stay on the charts.

```python
# Convert Weeks Charted to numeric
df_1['Weeks Charted'] = pd.to_numeric(df_1['Weeks Charted'], errors='coerce')
print(df_1['Weeks Charted'].describe())
```

### 6. Artist Followers

While not directly related to song popularity, this could be an interesting target if you want to predict an artist's popularity based on their songs.

```python
print(df_1['Artist Followers'].describe())
```

### Analysis

After examining these potential targets, consider the following:

1. **Popularity** seems like the most direct measure of a song's success and is likely the best target for predicting overall popularity.

2. **Streams** could be a good alternative if you want to focus on a more concrete measure of engagement.

3. **Highest Charting Position** and **Number of Times Charted** could be good targets if you want to focus on chart performance specifically.

4. **Weeks Charted** could be interesting if you want to predict longevity on the charts.

5. **Artist Followers** could be a good target if you want to predict an artist's overall popularity based on their songs.

### Recommendation

Based on the information provided, I would recommend using **Popularity** as the primary target variable. It's already in a suitable format for regression tasks and seems to be the most direct measure of a song's popularity.

If you want to explore different aspects of popularity, you could consider using multiple targets and creating separate models for each. For example, you could have one model predicting overall popularity, another predicting streaming numbers, and another predicting chart performance.

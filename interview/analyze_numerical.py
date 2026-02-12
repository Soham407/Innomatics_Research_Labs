import pandas as pd

# Load the dataset
file_path = r'c:\Users\soham\Downloads\Data-GenAI\final_food_delivery_dataset.csv'
df = pd.read_csv(file_path)

# Data Processing
df['total_amount'] = pd.to_numeric(df['total_amount'], errors='coerce')
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

print("--- Numerical Results ---")

# 1. How many total orders were placed by users with Gold membership?
gold_orders_count = df[df['membership'] == 'Gold'].shape[0]
print(f"1. Gold Orders Count: {gold_orders_count}")

# 2. What is the total revenue (rounded to nearest integer) generated from orders placed in Hyderabad city?
hyderabad_revenue = df[df['city'] == 'Hyderabad']['total_amount'].sum()
print(f"2. Hyderabad Total Revenue: {round(hyderabad_revenue)}")

# 3. How many distinct users placed at least one order?
distinct_users = df['user_id'].nunique()
print(f"3. Distinct Users: {distinct_users}")

# 4. What is the average order value (rounded to 2 decimals) for Gold members?
gold_avg_value = df[df['membership'] == 'Gold']['total_amount'].mean()
print(f"4. Gold Avg Order Value: {round(gold_avg_value, 2)}")

# 5. How many orders were placed for restaurants with rating ≥ 4.5?
rating_4_5_orders = df[df['rating'] >= 4.5].shape[0]
print(f"5. Orders with rating >= 4.5: {rating_4_5_orders}")

# 6. How many orders were placed in the top revenue city among Gold members only?
gold_members = df[df['membership'] == 'Gold']
top_city = gold_members.groupby('city')['total_amount'].sum().idxmax()
top_city_gold_orders = gold_members[gold_members['city'] == top_city].shape[0]
print(f"6. Top Revenue City for Gold: {top_city}")
print(f"6. Orders in {top_city} by Gold members: {top_city_gold_orders}")

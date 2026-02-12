import pandas as pd
import numpy as np

# Load the dataset
file_path = r'c:\Users\soham\Downloads\Data-GenAI\final_food_delivery_dataset.csv'
df = pd.read_csv(file_path)

# Data Processing
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)
df['total_amount'] = pd.to_numeric(df['total_amount'], errors='coerce')
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

print("--- Analysis Results (Refined) ---")

# Q1
gold_members = df[df['membership'] == 'Gold']
q1 = gold_members.groupby('city')['total_amount'].sum().idxmax()
print(f"Q1: {q1}")

# Q2
q2 = df.groupby('cuisine')['total_amount'].mean().idxmax()
print(f"Q2: {q2}")

# Q3
user_totals = df.groupby('user_id')['total_amount'].sum()
q3_count = (user_totals > 1000).sum()
print(f"Q3 Count: {q3_count}")

# Q4
bins = [3.0, 3.6, 4.1, 4.6, 5.1]
labels = ['3.0 – 3.5', '3.6 – 4.0', '4.1 – 4.5', '4.6 – 5.0']
df['rating_range'] = pd.cut(df['rating'], bins=bins, labels=labels, right=False)
q4 = df.groupby('rating_range', observed=False)['total_amount'].sum().idxmax()
print(f"Q4: {q4}")

# Q5
q5 = gold_members.groupby('city')['total_amount'].mean().idxmax()
print(f"Q5: {q5}")

# Q6
cuisine_counts = df.groupby('cuisine')['restaurant_id'].nunique()
q6 = cuisine_counts.idxmin()
print(f"Q6: {q6}")

# Q7
gold_orders = len(df[df['membership'] == 'Gold'])
total_orders = len(df)
q7_pct = round((gold_orders / total_orders) * 100)
print(f"Q7: {q7_pct}%")

# Q8: Which restaurant has the highest avg order value but less than 20 total orders?
# Options: Grand Cafe Punjabi, Grand Restaurant South Indian, Ruchi Mess Multicuisine, Ruchi Foods Chinese
options_q8 = ['Grand Cafe Punjabi', 'Grand Restaurant South Indian', 'Ruchi Mess Multicuisine', 'Ruchi Foods Chinese']
q8_rest_stats = df[df['restaurant_name'].isin(options_q8)].groupby('restaurant_name').agg(
    avg_order_value=('total_amount', 'mean'),
    order_count=('order_id', 'count')
)
print("Q8 Stats for options:")
print(q8_rest_stats)
q8_filtered = q8_rest_stats[q8_rest_stats['order_count'] < 20]
if not q8_filtered.empty:
    q8 = q8_filtered['avg_order_value'].idxmax()
    print(f"Q8: {q8}")
else:
    print("Q8: No option has less than 20 orders.")

# Q9: Which combination contributes the highest revenue?
# Options: Gold + Indian cuisine, Gold + Italian cuisine, Regular + Indian cuisine, Regular + Chinese cuisine
options_q9 = [
    ('Gold', 'Indian'),
    ('Gold', 'Italian'),
    ('Regular', 'Indian'),
    ('Regular', 'Chinese')
]
rev_q9 = df.groupby(['membership', 'cuisine'])['total_amount'].sum().reset_index()
print("Q9 Results for options:")
for m, c in options_q9:
    val = rev_q9[(rev_q9['membership'] == m) & (rev_q9['cuisine'] == c)]['total_amount'].values[0]
    print(f"{m} + {c}: {val:.2f}")

# Q10
df['quarter'] = df['order_date'].dt.quarter
q10 = df.groupby('quarter')['total_amount'].sum().idxmax()
print(f"Q10: Q{q10}")

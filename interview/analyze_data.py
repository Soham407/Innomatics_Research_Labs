import pandas as pd

def analyze_dataset():
    df = pd.read_csv(r'c:\Users\soham\Downloads\Data-GenAI\final_food_delivery_dataset.csv')
    
    # Convert order_date to datetime
    # Looking at the sample, format seems to be DD-MM-YYYY
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)
    
    analysis = {}
    
    # 1. Order trends over time (Monthly)
    analysis['order_trends'] = df.resample('ME', on='order_date').size()
    
    # 2. User behavior patterns (Average spend)
    analysis['avg_spend_per_user'] = df.groupby('user_id')['total_amount'].mean().mean()
    analysis['avg_orders_per_user'] = df.groupby('user_id').size().mean()
    
    # 3. City-wise and cuisine-wise performance
    analysis['city_performance'] = df.groupby('city')['total_amount'].sum().sort_values(ascending=False)
    analysis['cuisine_performance'] = df.groupby('cuisine')['total_amount'].sum().sort_values(ascending=False)
    
    # 4. Membership impact
    membership_impact = df.groupby('membership').agg({
        'total_amount': ['sum', 'mean', 'count'],
        'user_id': 'nunique'
    })
    # Calculate spend per unique user
    membership_impact['spend_per_user'] = membership_impact[('total_amount', 'sum')] / membership_impact[('user_id', 'nunique')]
    analysis['membership_impact'] = membership_impact
    
    # 5. Revenue distribution and seasonality (Monthly Revenue)
    analysis['monthly_revenue'] = df.resample('ME', on='order_date')['total_amount'].sum()
    
    print("--- ANALYSIS RESULTS ---")
    print("\n1. Order Trends (Monthly Counts):")
    print(analysis['order_trends'])
    
    print("\n2. User Behavior:")
    print(f"Average Spend per Order: {df['total_amount'].mean():.2f}")
    print(f"Average Orders per User: {analysis['avg_orders_per_user']:.2f}")
    
    print("\n3. City Performance (Revenue):")
    print(analysis['city_performance'])
    
    print("\n4. Cuisine Performance (Revenue):")
    print(analysis['cuisine_performance'])
    
    print("\n5. Membership Impact:")
    print(analysis['membership_impact'])
    
    print("\n6. Monthly Revenue:")
    print(analysis['monthly_revenue'])

if __name__ == "__main__":
    analyze_dataset()

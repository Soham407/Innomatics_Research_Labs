import pandas as pd
import json
import re

def create_final_dataset():
    # Step 1: Load CSV Data
    orders_df = pd.read_csv(r'c:\Users\soham\Downloads\Data-GenAI\orders.csv')
    
    # Step 2: Load JSON Data
    with open(r'c:\Users\soham\Downloads\Data-GenAI\users.json', 'r') as f:
        users_data = json.load(f)
    users_df = pd.DataFrame(users_data)
    
    # Step 3: Load SQL Data
    with open(r'c:\Users\soham\Downloads\Data-GenAI\restaurants.sql', 'r') as f:
        sql_content = f.read()
    
    # Simple regex to extract data from INSERT INTO statements
    # Pattern: VALUES (id, 'name', 'cuisine', rating);
    pattern = r"INSERT INTO restaurants VALUES \((\d+), '(.*?)', '(.*?)', ([\d\.]+)\);"
    matches = re.findall(pattern, sql_content)
    
    restaurants_df = pd.DataFrame(matches, columns=['restaurant_id', 'restaurant_name_sql', 'cuisine', 'rating'])
    restaurants_df['restaurant_id'] = restaurants_df['restaurant_id'].astype(int)
    restaurants_df['rating'] = restaurants_df['rating'].astype(float)
    
    # Step 4: Merge the Data
    # orders.user_id -> users.user_id
    # orders.restaurant_id -> restaurants.restaurant_id
    
    # First join orders with users
    merged_df = pd.merge(orders_df, users_df, on='user_id', how='left', suffixes=('', '_user'))
    
    # Then join with restaurants
    final_df = pd.merge(merged_df, restaurants_df, on='restaurant_id', how='left', suffixes=('', '_rest'))
    
    # The final dataset contains: Order details, User information, Restaurant information
    # Ensure correct columns and clean up if needed
    # User might want to keep the restaurant_name from the SQL file if it differs from orders.csv
    # Based on the view_file, orders.csv has restaurant_name like 'New Foods Chinese' 
    # while sql has 'Restaurant_1'. The user request says "orders.restaurant_id -> restaurants.restaurant_id"
    
    # Step 5: Save to Output File
    final_df.to_csv(r'c:\Users\soham\Downloads\Data-GenAI\final_food_delivery_dataset.csv', index=False)
    print("Final dataset created successfully.")

if __name__ == "__main__":
    create_final_dataset()

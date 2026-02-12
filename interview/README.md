# Food Delivery Data Analysis & Generation

A comprehensive data engineering and analysis project focused on understanding food delivery patterns, user behavior, and restaurant performance. This repository includes scripts for data generation (merging multiple sources) and detailed analysis using Python and Pandas.

## 🚀 Overview

The project demonstrates a realistic workflow for:

1.  **Data Integration**: Merging data from CSV (Orders), JSON (Users), and SQL (Restaurants).
2.  **Data Cleaning**: Normalizing timestamps, handling numerical conversions, and cleaning text data.
3.  **Advanced Analytics**: Answering complex business questions regarding revenue, membership tiers, and geographic performance.

## 📁 Project Structure

- `create_dataset.py`: The data pipeline script that merges `orders.csv`, `users.json`, and `restaurants.sql` into the master dataset.
- `analyze_data.py`: Provides high-level analysis of order trends, user behavior, city performance, and the impact of membership tiers.
- `analyze_numerical.py`: focused on providing specific numerical answers like total revenue in Hyderabad or order counts for Gold members.
- `analyze_results.py`: A deep-dive analysis script that solves specific multi-part business questions (e.g., highest revenue cuisine, top-performing quarters).
- `final_food_delivery_dataset.csv`: The resulting master dataset containing all merged and cleaned information.
- `Soham.ipynb`: An interactive Jupyter Notebook for exploratory data analysis (EDA).

## 🛠️ Getting Started

### Prerequisites

- Python 3.x
- Pandas
- NumPy

### Installation

Clone the repository:

```bash
git clone https://github.com/Soham407/Innomatics_Research_Labs.git
cd Innomatics_Research_Labs
```

### Usage

1.  **Generate the Dataset**:
    If you have the source files (`orders.csv`, `users.json`, `restaurants.sql`), run:
    ```bash
    python create_dataset.py
    ```
2.  **Run Analysis**:
    To see the analysis results, execute any of the following:
    ```bash
    python analyze_data.py
    python analyze_numerical.py
    python analyze_results.py
    ```

## 📊 Sample Insights

Some of the key metrics covered in the analysis:

- **Top Revenue Cities**: Identifying which cities generate the most revenue from Gold members.
- **Cuisine Popularity**: Finding cuisines with the highest average order value.
- **Seasonal Trends**: Determining the quarter with the highest total revenue.
- **Membership Value**: Quantifying the percentage of orders coming from Gold vs. Regular members.

## 📄 License

This project is for educational purposes.

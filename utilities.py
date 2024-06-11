import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def summarize_df(df):
    """Generates a summary of the given DataFrame, including the column names, non-null counts,
    missing values, percentage of missing values, data types, and the number of unique values."""

    summary = pd.DataFrame({
        'Column': df.columns,
        'Non-Null Count': df.notnull().sum(),
        'Missing Values': df.isnull().sum(),
        'Missing Values (%)': (df.isnull().mean() * 100).round(2),
        'Dtype': df.dtypes,
        'Unique Values': df.nunique()
    })
    return summary.reset_index(drop=True)

def summarize_object_columns(df):
    summary = {}
    for col in df.select_dtypes(include=['object']).columns:
        value_counts = df[col].value_counts()
        unique_values = value_counts.index.tolist()
        counts = value_counts.values.tolist()
        summary[col] = {
            "Unique Values Count": len(unique_values),
            "Top 5 Values": unique_values[:5],
            "Top 5 Counts": counts[:5],
            "Total Unique Values": unique_values
        }
    return summary

def plot_counts(df, columns, title):
    """
    Plots horizontal bar plots for the value counts of specified columns in a DataFrame.

    Args:
    df (pd.DataFrame): The DataFrame containing the data.
    columns (list): The list of column names to plot.
    title (str): The title of the plot.

    Returns:
    None
    """
    plt.figure(figsize=(15, 10))
    for i, col in enumerate(columns):
        plt.subplot(2, 2, i + 1)
        df[col].value_counts().sort_values(ascending=True).plot(kind='barh', color='skyblue')
        plt.title(col)
        plt.ylabel('Subtype')
        plt.xlabel('Count')
    plt.suptitle(title)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def get_unique_card_counts(df, group_by_columns):
    """
    Group the DataFrame by card_type_id and the specified columns to get the count of unique cards.

    Args:
    df (pd.DataFrame): The DataFrame containing the data.
    group_by_columns (list): The list of column names to group by.

    Returns:
    pd.DataFrame: A DataFrame with the count of unique cards grouped by the specified columns.
    """
    # Group by card_type_id to ensure uniqueness
    unique_cards = df.groupby(['card_type_id'] + group_by_columns).size().reset_index(name='count')
    
    # Group by the desired columns to get the count of unique cards
    return unique_cards.groupby(group_by_columns).size().unstack()

def get_unique_card_prices(df):
    """
    Group the DataFrame by card_type_id and release_year to calculate the mean market price for unique cards.

    Args:
    df (pd.DataFrame): The DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the mean market prices for unique cards grouped by card_type_id and release_year.
    """
    # Group by card_type_id and release_year to ensure uniqueness
    unique_cards = df.groupby(['card_type_id', 'release_year'])['market'].mean().reset_index()
    return unique_cards

def plot_prices(df, price_column='market', plot_type='both'):
    """
    Plot the mean and median market prices by year.

    Args:
    df (pd.DataFrame): The DataFrame containing the data.
    price_column (str): The name of the column containing the prices. Default is 'market'.
    plot_type (str): The type of plot to generate ('mean', 'median', or 'both'). Default is 'both'.

    Returns:
    None
    """
    # Get the unique card prices
    unique_card_prices = get_unique_card_prices(df)

    # Group by year and calculate the mean and median market prices
    mean_price_by_year = unique_card_prices.groupby('release_year')[price_column].mean()
    median_price_by_year = unique_card_prices.groupby('release_year')[price_column].median()

    plt.figure(figsize=(15, 8))

    # Define the width of the bars
    bar_width = 0.4
    positions = np.arange(len(mean_price_by_year))

    if plot_type in ['mean', 'both']:
        plt.bar(positions - (bar_width/2 if plot_type == 'both' else 0), mean_price_by_year, 
                width=(bar_width if plot_type == 'both' else bar_width*2), color='skyblue', label='Mean')
    if plot_type in ['median', 'both']:
        plt.bar(positions + (bar_width/2 if plot_type == 'both' else 0), median_price_by_year, 
                width=(bar_width if plot_type == 'both' else bar_width*2), color='salmon', label='Median')

    # Plot title and labels
    plt.title('Market Price by Year')
    plt.xlabel('Year')
    plt.ylabel('Market Price')
    plt.xticks(positions, mean_price_by_year.index, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_price_buckets(df, columns, top_n=None, show_proportion=True):
    """
    Plot the distribution of price buckets for each specified column, optionally limited to the top N values.

    Args:
    df (pd.DataFrame): The DataFrame containing the data.
    columns (list): The list of column names to plot.
    top_n (int, optional): The number of top values to plot based on the highest proportions of the 'high' price bucket.
    show_proportion (bool): Whether to show proportions or counts. Default is True (show proportions).

    Returns:
    None
    """
    for column in columns:
        if top_n:
            # Get the top N values for the column
            top_values = df[column].value_counts().nlargest(top_n).index
            plot_df = df[df[column].isin(top_values)]
        else:
            plot_df = df

        unique_values = plot_df[column].nunique()

        if show_proportion:
            bucket_counts = plot_df.groupby(column)['price_bucket'].value_counts(normalize=True).unstack().fillna(0) * 100
            # Sort the values by the proportion of the 'high' price bucket
            bucket_counts = bucket_counts.sort_values(by='high', ascending=True)
            ylabel = 'Proportion (%)'
        else:
            bucket_counts = plot_df.groupby(column)['price_bucket'].value_counts().unstack().fillna(0)
            bucket_counts = bucket_counts.loc[bucket_counts.sum(axis=1).sort_values(ascending=True).index]
            ylabel = 'Count'

        if unique_values > 5:
            plt.figure(figsize=(12, 10))
            bucket_counts.plot(kind='barh', stacked=True, figsize=(12, 10), color=['skyblue', 'salmon'], width=0.8)
            plt.xlabel(ylabel)
            plt.ylabel(column.capitalize())
        else:
            plt.figure(figsize=(8, 6))
            bucket_counts.plot(kind='bar', stacked=True, figsize=(8, 6), color=['skyblue', 'salmon'], width=0.8)
            plt.ylabel(ylabel)
            plt.xlabel(column.capitalize())
            plt.xticks(rotation=0)

        # Plot title and labels
        plt.title(f'Price Bucket Distribution by {column.capitalize()}' + (f' (Top {top_n})' if top_n else ''))
        plt.legend(title='Price Bucket')
        plt.tight_layout()
        plt.show()


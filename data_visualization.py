"""
This module contains functions to visualize data using matplotlib and pandas.
"""
import os

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from  dotenv import  load_dotenv

load_dotenv()
PLOT_PATH = Path(os.getenv("PLOT_PATH"))

def plot_gender_pie(df: pd.DataFrame , output_path: str = PLOT_PATH) -> None:
    """
    Pie chart of gender distribution.
    :param df: pd.DataFrame
    :param output_path: str
    :return: None
    """
    counts = df["gender"].value_counts()
    plt.figure()
    plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Gender Distribution')
    plt_path = os.path.join(output_path,"plot_gender_pie")
    plt.savefig(plt_path)

def plot_gender_hist_by_country(df: pd.DataFrame , output_path: str = PLOT_PATH) -> None:
    """
    Histogram of gender variation by country.
    :param df: pd.DataFrame
    :param output_path: str
    :return: if output_path is None, show the plot, else save it to the path
    """
    grp = df.groupby(['location_country', 'gender']).size().unstack(fill_value=0)
    pct = grp.div(grp.sum(axis=1), axis=0) * 100
    pct.plot(kind='bar', color=['#1f77b4', '#ff7f0e'])
    plt.xlabel('Country')
    plt.ylabel('Percentage')
    plt.title('Gender Percentage by Country')
    plt.legend(title='Gender')
    plt.tight_layout()
    plt_path = os.path.join(output_path,"plot_gender_hist_by_country")
    plt.savefig(plt_path)

def plot_age_distribution_bar(df: pd.DataFrame , output_path: str = PLOT_PATH) -> None:
    """
    Bar chart of age distribution.
    :param df: pd.DataFrame
    :param output_path: str
    :return: if output_path is None, show the plot, else save it to the path
    """
    counts = df['dob_age'].value_counts().sort_index()
    plt.figure()
    counts.plot(kind='bar', color='#2ca02c')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Age Distribution')
    plt.tight_layout()
    plt_path = os.path.join(output_path, "plot_age_distribution_bar")
    plt.savefig(plt_path)

def plot_usage_vs_avg(df: pd.DataFrame, output_path: str = PLOT_PATH) -> None:
    """
    Histogram of usage years with average line.
    :param df: pd.DataFrame
    :param output_path: str
    :return: if output_path is None, show the plot, else save it to the path
    """
    values = df['registered_age']
    avg = values.mean()
    plt.figure()
    plt.hist(values, bins=10, color='#d62728', alpha=0.7)
    plt.axvline(avg, color='black', linestyle='dashed', linewidth=1.5, label=f'Avg = {avg:.2f}')
    plt.xlabel('Usage Years')
    plt.ylabel('Count')
    plt.title('Usage Years Distribution vs Average')
    plt.legend()
    plt.tight_layout()
    plt_path = os.path.join(output_path, "plot_usage_vs_avg")
    plt.savefig(plt_path)

def plot_country_distribution_pie(df: pd.DataFrame, output_path: str = PLOT_PATH) -> None:
    """
    Pie chart of country distribution.
    :param df: pd.DataFrame
    :param output_path: str
    :return: if output_path is None, show the plot, else save it to the path
    """
    counts = df['location_country'].value_counts()
    plt.figure()
    explode = [0.3 if country == "Turkey" else 0.0 for country in counts.index]
    plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%', startangle=90, explode=explode)
    plt.title('Country Distribution')
    plt_path = os.path.join(output_path, "plot_country_distribution_pie")
    plt.savefig(plt_path)



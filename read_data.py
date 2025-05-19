"""
This module is responsible for fetching user data from the API, flattening the data and saving it in parquet format.
It also includes functions to check if the data exists, delete existing data, and load the data from the parquet file.
"""


import os
from typing import List, Any
import pandas
import pandas as pd
import requests
from time import time, sleep
from pathlib import Path

DATA_PATH = Path("./data/")

def is_data_exists() -> bool:
    """
    Check user.parquet file if it's exists or not
    :return: bool
    """
    relative_path = Path.joinpath(DATA_PATH, "user.parquet")
    if relative_path.exists():
        return True
    return False


def delete_existing_user_data():
    """
    Delete user.parquet file if exists
    :return: None
    """
    relative_path = Path.joinpath(DATA_PATH, "user.parquet")
    if is_data_exists():
        os.remove(relative_path)



def load_data() -> pandas.DataFrame:
    """
    Load parquet file from file path
    :return : return pandas.DataFrame
    """
    relative_path = Path.joinpath(DATA_PATH, "user.parquet")
    df = pd.read_parquet(relative_path)
    return df


def flatten_and_drop_unused_columns(data_list: List[Any]) -> pandas.DataFrame:
    """
    Make data flatten and drop unused columns from data.
    :param data_list:List[Any]: input for any kind of list
    :return : pandas.Dataframe
    """
    organized_data = []

    for user in data_list:
        flat_user = {
            'gender': user['gender'],
            'name_title': user['name']['title'],
            'name_first': user['name']['first'],
            'name_last': user['name']['last'],
            'location_street_number': user['location']['street']['number'],
            'location_street_name': user['location']['street']['name'],
            'location_city': user['location']['city'],
            'location_state': user['location']['state'],
            'location_country': user['location']['country'],
            'location_postcode': str(user['location']['postcode']),
            'email': user['email'],
            'picture': user['picture']['medium'],
            'dob_date': user['dob']['date'],
            'dob_age': user['dob']['age'],
            'registered_date': user['registered']['date'],
            'registered_age': user['registered']['age'],
            'phone': user['phone'],
            'cell': user['cell'],
            'nat': user['nat']
        }
        organized_data.append(flat_user)
    df = pd.DataFrame(organized_data)

    df['dob_date'] = pd.to_datetime(df['dob_date']).dt.strftime('%Y-%m-%d %H:%M:%S')
    df['registered_date'] = pd.to_datetime(df['registered_date']).dt.strftime('%Y-%m-%d %H:%M:%S')
    return df


def save_data(df: pandas.DataFrame):
    """
    Take dataframe and save as parquet format to the path
    :param df: pandas.DataFrane
    :return: None
    """
    relative_path = Path.joinpath(DATA_PATH, "user.parquet")
    try:
        df.to_parquet(relative_path,index=False,engine='auto')
    except Exception as e:
        print("Parquet dosyası oluşturulurken hata oluştu ", e)


def get_data(read_new_data: bool = False , get_data_min: float = 10) -> pandas.DataFrame:
    """
    Get data from https://randomuser.me/api/
    :param read_new_data : user input for fetching new data
    :param get_data_min : how many minutes to fetch
    :return : pandas.DataFrame
    """
    data_list = []
    end_time = time() + int(get_data_min * 60)

    if read_new_data:
        while time() < end_time:
            try:
                response = requests.get("https://randomuser.me/api/")
                if response.status_code == 200:
                    user_data = response.json()["results"][0]
                    data_list.append(user_data)
                else:
                    print(f"Hata {response.status_code}")
            except Exception as e:
                print("Hata oluştu, ", e)
            sleep(2)
        delete_existing_user_data()
        df  = flatten_and_drop_unused_columns(data_list)
        save_data(df)
    else:
        res = is_data_exists()
        if not res:
            raise Exception("Please download your data first")
        df = load_data()
    return df
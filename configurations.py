import os

def get_file_path() -> str:
    """
    Get the file path for the parquet file.
    :return: str
    """
    data_path= os.getenv("DATA_PATH")
    parquet_file_name=os.getenv("PARQUET_FILE_NAME")
    file_path=os.path.join(data_path,parquet_file_name)
    file_path+=".parquet"
    return file_path

def check_directory_exists(directory: str) -> bool:
    """
    Check if the directory exists.
    :param directory: str
    :return: bool
    """
    return os.path.exists(directory)

def create_directory(directory: str) -> None:
    """
    Create a directory if it does not exist.
    :param directory: str
    :return: None
    """
    if not check_directory_exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    else:
        print(f"Directory '{directory}' already exists.")
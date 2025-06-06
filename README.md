## Data Analysis Project

A comprehensive data analysis platform built with PySpark, designed for efficient data processing and visualization.

### Introduction

This project is a data analysis solution that:
- Utilizes PySpark for high-performance data processing and analysis
- Runs in a Docker container for consistent deployment across environments
- Features dedicated modules for data ingestion, analysis, and visualization
- Provides a convenient CLI interface for executing various data operations

###  Requirements

#### Core Dependencies
- Docker
  - PySpark Docker image
- Python 3.9

#### Python Packages
- PySpark 3.5.5
- Pandas 2.2.3
- PyArrow 20.0.0
- Requests 2.32.3
- Click 8.1.8
- Matplotlib 3.9.4
- NumPy 2.0.2

###  Project Structure

```
data-analysis/
├── data/
├── plots/
├── configurations.py
├── data_visualization.py
├── docker-compose.yml
├── env.template
├── main.py
├── pyspark_analyzer.py
├── read_data.py
├── README.md
├── requirements.txt
├── test_column_flatten.py
└── user_data_analysis.py
```

###  Installation

1. **Clone the repository**

2. **Create a Python virtual environment** (optional)
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```
4. **Create .env file**
   ```bash
   touch .env
   ```
5. **Copy variables from env.template file and write your own paths**
   ```bash
   vim .env
   ```
   - When vim editor opens, press `i` to enter insert mode , then copy the variables from `env.template` and modify them as needed.
   - After editing, press `Esc`, type `:wq`, and hit `Enter` to save and exit.
5. **Install Docker desktop if not already installed.It's required to run apache spark**
   ```bash
    https://www.docker.com/products/docker-desktop
   ```
### Run the project

   ####  Run Docker Container

   1. **Build the Docker image**
   ```bash
   docker-compose build
   ```

   2. **Run the Docker container**

      Docker compose needs `.env ` file to get data folder. If `.env` files is located in same folder with `docker-compose.yml` file then you can run the command below: 
      ```bash
      docker-compose up -d
      ```
   
      If not located in the same folder, you can specify the path to the `.env` file using the `--env-file` option:
   
      ```bash
      docker-compose --env-file /path/to/your/.env up -d
      ```

   3. **Incase if needed to stop the Docker container**
      ```bash
      docker-compose down
      ```

- **Run Python code**

   After the Docker container is running, you can execute 
```bash
   python main.py --help
 ```

###  Command Line Interface

#### `read_data`
**Description:** Reads data from API and saves it in parquet format

**Options:**
- `--new-data`: Read new data from API instead of using cached data
- `--min-data MIN_DATA`: Set minimum amount of data to read (default: 1)
- `--verbose`: Show detailed information about the data

**Usage:**
```bash
python main.py read_data [--new-data] [--min-data MIN_DATA] [--verbose]
```

#### `solve`
**Description:** Solve specific questions based on the question ID

**Options:**
- `--question-id QUESTION_ID`: ID of the question to solve (required)
- `--verbose`: Show detailed information during solving

**Usage:**
```bash
python main.py solve --question-id QUESTION_ID [--verbose]
```

#### `visualize`
**Description:** Perform exploratory data analysis (EDA) on the data

**Options:**
- `--plot_path PLOT_PATH`: Path to the plot directory

**Usage:**
```bash
python main.py visualize --plot_path PLOT_PATH
```

#### `create`
**Description:** Create plots and save them to the specified path

**Options:**
- `--plot_path PLOT_PATH`: Path to the plot directory

**Usage:**
```bash
python main.py create --plot_path PLOT_PATH
```

#### `check-plots`
**Description:** Check if the plots have been created successfully

**Options:**
- `--plot_path PLOT_PATH`: Path to the plot directory

**Usage:**
```bash
python main.py check-plots --plot_path PLOT_PATH
```
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

4. **Run the project**
   ```bash
   python main.py
   ```

###  Docker Deployment

1. **Build the Docker image**
   ```bash
   docker-compose build
   ```

2. **Run the Docker container**
   ```bash
   docker-compose up -d
   ```

3. **Stop the Docker container**
   ```bash
   docker-compose down
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

### `solve`
**Description:** Solve specific questions based on the question ID

**Options:**
- `--question-id QUESTION_ID`: ID of the question to solve (required)
- `--verbose`: Show detailed information during solving

**Usage:**
```bash
python main.py solve --question-id QUESTION_ID [--verbose]
```

### `visualize`
**Description:** Perform exploratory data analysis (EDA) on the data

**Options:**
- `--plot_path PLOT_PATH`: Path to the plot directory

**Usage:**
```bash
python main.py visualize --plot_path PLOT_PATH
```

### `create`
**Description:** Create plots and save them to the specified path

**Options:**
- `--plot_path PLOT_PATH`: Path to the plot directory

**Usage:**
```bash
python main.py create --plot_path PLOT_PATH
```

### `check-plots`
**Description:** Check if the plots have been created successfully

**Options:**
- `--plot_path PLOT_PATH`: Path to the plot directory

**Usage:**
```bash
python main.py check-plots --plot_path PLOT_PATH
```
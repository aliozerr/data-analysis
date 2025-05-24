"""
This module includes click functions to create a command line interface (CLI) for the user data analysis project.
It allows users to fetch data from an API, solve specific questions, visualize data, create plots, and check for missing plots.
The CLI is built using the Click library, which provides a simple way to create command line interfaces.
The CLI includes the following commands:
   - `get-data`: Fetch data from the API and save it in parquet format.
   - `solve`: Solve specific questions based on the data.
   - `visualize`: Perform exploratory data analysis (EDA) on the data.
   - `create`: Create plots and save them to a specified directory.
   - `check-plots`: Check if the plots have been created successfully.
"""

import click
from configurations import *
from user_data_analysis import read_data,solve_question, visualize_plot, plot_creation,check_missing_plots
from dotenv import  load_dotenv
load_dotenv()


@click.group(help="A CLI tool that includes commands to run and visualize command.")
def cli():
    pass

@cli.command(name='get-data', help=":Fetch data from API" )
@click.option("--new_data",default=False, help="read new data from api")
@click.option("--data_min",default=1, help="read data from api that minute")
@click.option("--verbose",default=False, help="print with verbose option")
def get_data(new_data, data_min,verbose) -> None:
    """
    Fetch data from API and save it in parquet format.
    :param new_data:
    :param data_min:
    :param verbose:
    :return: None
    """
    print(get_file_path())
    read_data(new_data,data_min,verbose)



@cli.command(name='solve', help=":Solve the questions with given id" )
@click.option('--question',multiple=True, default=(1,2,3), help="question id to solve, e.g., default all")
@click.option("--verbose",default=False, help="print with verbose option")
def solve(question,verbose) -> None:
    """
    Solve specific questions based on the data.
    :param question:
    :param verbose:
    :return: None
    """
    for q in question:
        solve_question(q,verbose)



@cli.command(name='visualize', help=":Do some eda" )
@click.option('--plot_path' , help="Path to the plot directory.")
def visualize(plot_path) -> None:
    """
    Perform exploratory data analysis (EDA) on the data.
    :param plot_path: Path to the plot directory.
    :return : None
    """
    visualize_plot(plot_path)

@cli.command(name="create", help = ":Create plots and save it to the path")
@click.option("--plot_path",help = "Path to the plot directory ")
def create_plots(plot_path) -> None:
    """
    Create plots and save them to the specified path.
    :param plot_path:
    :return: None
    """
    plot_creation(plot_path)


@cli.command("check-plots", help = ":Check if the plots are created or not")
@click.option("--plot_path",help = "Path to the plot directory ")
def check_plots(plot_path) -> None:
    """
    Check if the plots have been created successfully.
    :param plot_path:
    :return: None
    """
    check_missing_plots(plot_path)

if __name__ == '__main__':
    cli()
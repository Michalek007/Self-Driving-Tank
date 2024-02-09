# Self-driving-tank API

Functionalities:
* controlling tank via graphical interface
* gathering acceleration, velocity and position data 
* updating graphs with current data in real time
* displaying collected data in graphs & tables

## Requirements

Python 3.8+

## Installation

First, clone this repository.

    $ git clone https://github.com/Michalek007/Self-Driving-Tank.git

After, to install virtual environment with all necessary packages run:

    $ venvSetup.bat

## Starting Application

To run development server run:
    
    $ py run.py

To run production server run:
    
    $ run.bat

or

    $ py server.py

To see your application, access this url in your browser: 

	http://127.0.0.1:5000

Or different url defined in `configuration.py` as variable `LISTENER`.

## Application development

To activate virtual environment in terminal run:
    
    $ ".venv\Scripts\activate.bat"

To install new package run:
    
    $ pipenv install <package_name>

## Project structure
    
Rest-api is dived into subdirectories which contains:
* **app** - Flask app, views & APScheduler
* **database** - SQLAlchemy database, schemas and data.db
* **tests** - tests for all service functionalities

All configuration is in: `configuration.py`. 
Configuration, requirements and run files are placed in the main directory.
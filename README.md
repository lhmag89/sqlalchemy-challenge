# sqlalchemy-challenge
This is a project to analyze temperature and precipitation data using SQLalchemy and python

## Technologies
python, Flask, SQLalchemy, excel, jupyter

## Installation Guide
Open a Jupyter notebook to run climate.ipynb. Run app.py using python. Make sure the resources folder is in the correct relative location.

## Usage
Running climate.ipynb in a Jupyter notebook should generate graphs below to analyze the data. Analysis includes determining the number of stations capturing observations, the most active station, determining preciptation over a date range and frequency of temperatures observed.

Running app.py file allows the following routes:

1. /api/v1.0/precipitation - Returns jsonified data with date as key and precipitation as value
2. /api/v1.0/stations - Returns list of stations
3. /api/v1.0/tobs - returns jsonified data for the last year of data for most active station (USC00519281)
4./api/v1.0/YYYY-MM-DD - Allows user to enter start date to retrieve minimum temperature, maximum temperature and average temperature observed
5. /api/v1.0/YYYY-MM-DD/YYYY-MM-DD> - Allows user to enter start and end date to retrieve minimum temperature, maximum temperature and average temperature observed
![image](https://user-images.githubusercontent.com/119267098/221122227-b3a5861f-8b7d-4f1f-8771-bf3495acace0.png)

![image](https://user-images.githubusercontent.com/119267098/221122188-0878e2a2-89e7-4696-9bdf-49153fed9417.png)


## Contributors
Developed by Luis Hernandez Email: lhernandez.mag.89@gmail.com

## License
UC Berkeley Extension Data Analytics Program

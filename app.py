# Import dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
station = Base.classes.station
measurement = Base.classes.measurement

# Flask Setup

app = Flask(__name__)

#Flask Routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/YYYY-MM-DD --> Enter start date<br/>"
        f"/api/v1.0/YYYY-MM-DD/YYYY-MM-DD> --> Enter start and end dates"
    )
@app.route("/api/v1.0/precipitation")
def prcp():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list dates with precipitation"""
    # Query dates over the most recent year
    results  = session.query(measurement.date, measurement.prcp).filter(measurement.date <= '2017-08-23').\
        filter(measurement.date > '2016-08-23')

    session.close()
    # Create a dictionary from the row data and append to a list of recent precipitation
    recent_prcp = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        recent_prcp.append(prcp_dict)
    return jsonify(recent_prcp)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations"""
    # Groupby station names to identify stations
    results  = session.query(measurement.station).group_by(measurement.station).all()

    session.close()
    # Create a list of stations
    stations = list(np.ravel(results))
    
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of temperature observations from most active station for last year"""
    # Query dates over the most recent year
    results  = session.query(measurement.date, measurement.tobs).filter(measurement.station == 'USC00519281').filter(measurement.date <= '2017-08-23').\
        filter(measurement.date > '2016-08-23').all()

    session.close()
    # Create a list of temperature observations over time
    recent_tobs = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        recent_tobs.append(tobs_dict)
    
    return jsonify(recent_tobs)

@app.route("/api/v1.0/<startdt>")
def startdata(startdt):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of minimum, maximum and average temperature observations from start date input"""
    # Query dates starting with input
    tmin = session.query(func.min(measurement.tobs)).filter(measurement.date > startdt).scalar()
    tmax = session.query(func.max(measurement.tobs)).filter(measurement.date > startdt).scalar()
    tavg = session.query(func.avg(measurement.tobs)).filter(measurement.date > startdt).scalar()

    session.close()
    # Create a list of stats
    tempdata = [tmin, tmax, tavg]
    
    return jsonify(tempdata)

@app.route("/api/v1.0/<startdt>/<enddt>")
def rangedata(startdt, enddt):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of minimum, maximum and average temperature observations from range of dates input"""
    # Query dates within range input
    tmin = session.query(func.min(measurement.tobs)).filter(measurement.date > startdt).filter(measurement.date <= enddt).scalar()
    tmax = session.query(func.max(measurement.tobs)).filter(measurement.date > startdt).filter(measurement.date <= enddt).scalar()
    tavg = session.query(func.avg(measurement.tobs)).filter(measurement.date > startdt).filter(measurement.date <= enddt).scalar()

    session.close()
    # Create a list of stats
    tempdata = [tmin, tmax, tavg]
    
    return jsonify(tempdata)

if __name__ == '__main__':
    app.run(debug=True)

import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, MetaData, Table
from flask import Flask, jsonify
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///happiness_db.db")
insp = inspect(engine)
# print(insp.get_table_names())

metadata = MetaData(engine)
metadata.reflect(bind=engine)
# print(metadata.tables)

Happiness = metadata.tables['happiness_database']

print(Happiness)
# reflect an existing database into a new model
# Base = automap_base()
# reflect the tables
# Base.prepare(engine, reflect=True)
# Save references to each table
# analysis = Base.classes.happiness 

# Create our session (link) from Python to the DB
session = Session(engine)
#################################################
# Flask Setup
app = Flask(__name__)
#################################################
# Flask Routes
@app.route("/")
def welcome():
    return (
        f"Welcome to our Happiness API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/dataframe<br/>")

@app.route("/api/v1.0/dataframe")
def dataframe():
    results = session.query(Happiness).all()
    # print(results)
    # Unravel results into a 1D array and convert to a list
    # data = list(np.ravel(results))
    return jsonify(results)

if __name__ == '__main__':
    app.run()

from .measurement import Measurement
from flask import request
from werkzeug.exceptions import abort
from .validation import datetime_in_range

measurements = []

def add_measurement(measurement):
    #add measurement if does not exist
    if get_measurement(measurement) == None:
        measurements.append(measurement)
    return measurement

def get_measurement(date):
    for m in measurements:
        if m.timestamp == date:
            return m
    return None
    
def delete_measurement(date):
    #delete measurement if exists
    delete_this_measurement = get_measurement(date)
    if delete_this_measurement is not None:
        measurements.remove(delete_this_measurement)
    return delete_this_measurement
            
def query_measurements(start_date, end_date):
    #swap to and from datetimes if from_datetime is greater than to_datetime
    if start_date > end_date:
        temp = start_date
        start_date = end_date
        end_date = temp
    
    #retrieve measurements in date range
    queried_measurements = []
    for m in measurements:
        if datetime_in_range(start_date, end_date, m.timestamp):
            queried_measurements.append(m)
    return queried_measurements

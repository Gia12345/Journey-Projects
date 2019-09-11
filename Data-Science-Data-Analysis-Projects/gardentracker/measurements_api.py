from flask import request, jsonify
from flask.views import MethodView
from werkzeug.exceptions import abort
from .measurement import Measurement
from .measurement_store import add_measurement, get_measurement, delete_measurement
from .validation import is_number, get_formatted_time, get_metric_list, create_response
from weathertracker.utils.conversion import (
    convert_to_datetime,
    DatetimeConversionException,
)

metric_list = get_metric_list()

class MeasurementsAPI(MethodView):

    # features/01-measurements/01-add-measurement.feature
    def post(self):
        request_data = request.get_json()
        
        #check for valid timestamp
        if 'timestamp' not in request_data:
            return create_response(400, body={'message':'Timestamp must be included'})
        timestamp = request_data['timestamp']
        try:
            timestamp = convert_to_datetime(timestamp)
        except DatetimeConversionException:
            return create_response(400, body={'message':'Invalid timestamp'})
        
        #create dictionary of metrics if metric values are valid
        metrics = {}
        for metric in metric_list:
            if metric in request_data:
                metrics[metric] = request_data[metric]
                if not is_number(metrics[metric]):
                    return create_response(400, body={'message':'Invalid metric values'})
                    
        #create and add Measurement object
        add_measurement(Measurement(timestamp, metrics))
        
        #create and return response
        response = create_response(201)
        format_time = get_formatted_time(timestamp)
        response.location = '/measurements/'+ format_time
        return response

    # features/01-measurements/02-get-measurement.feature
    def get(self, timestamp):
        try:
            timestamp = convert_to_datetime(timestamp)
        except DatetimeConversionException:
            return create_response(400, body={'message': 'Invalid timestamp'})

        measurement = get_measurement(timestamp)
        
        #create and return response
        if measurement is None:
            return create_response(404, body={'message':'Measurement not found'})
        else:
            format_time = get_formatted_time(measurement.timestamp)
            body = {"timestamp": format_time,
                            "temperature": measurement.get_metric('temperature'),
                            "dewPoint": measurement.get_metric('dewPoint'),
                            "precipitation": measurement.get_metric('precipitation')
            }
            return create_response(200, body=body)

    # features/01-measurements/03-delete-measurement.feature
    def delete(self, timestamp):
        try:
            timestamp = convert_to_datetime(timestamp)
        except DatetimeConversionException:
            return create_response(400, body={'message': 'Invalid timestamp'})
            
        delete_result = delete_measurement(timestamp)
        
        #create and return response
        if delete_result is None:
            return create_response(404, body={'message':'Measurement not found'})
        else:
            return create_response(204)
   


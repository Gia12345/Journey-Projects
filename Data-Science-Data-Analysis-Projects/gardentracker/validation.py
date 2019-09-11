from statistics import mean
from flask import jsonify

def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
        
def get_formatted_time(timestamp):
    return timestamp.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    
def get_metric_list():
    return ['temperature', 'dewPoint', 'precipitation']
    
def get_stats_list():
    return {'average': mean, 'max': max, 'min': min}
    
def create_response(status_code, body=None):
    if body == None:
        response = jsonify()
    else:
        response = jsonify(body)
    response.status_code = status_code
    return response
    
def datetime_in_range(start, end, dt):
    return start <= dt < end


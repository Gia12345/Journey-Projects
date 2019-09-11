from werkzeug.exceptions import abort
from weathertracker.measurement_store import query_measurements
from statistics import mean
from .statistics import Statistics
from .validation import get_stats_list

stats_store = []
stats_dict = get_stats_list()

def get_statistic(from_datetime, to_datetime):
    for statistic in stats_store:
        if (statistic.from_datetime == from_datetime and statistic.to_datetime == to_datetime):
            return statistic
    return Statistics(from_datetime, to_datetime)

def get_stats(stats, metrics, from_datetime, to_datetime):
   #initialize metric_dict to hold list of values for each metric
    metric_dict = {}
    for metric in metrics:
        metric_dict[metric] = []
        
    #swap to and from datetimes if from_datetime is greater than to_datetime
    if from_datetime > to_datetime:
        temp = from_datetime
        from_datetime = to_datetime
        to_datetime = temp
    
    #create Statistics object or retrieve if already exsits
    new_statistic = get_statistic(from_datetime, to_datetime)

    #retrieve list of measurements and create list of values for each metric to add to metric_dict
    queried_measurements = query_measurements(from_datetime, to_datetime)
    for measurement in queried_measurements:
        for metric in metrics:
            if metric in measurement.metrics:
                metric_dict[metric].append(measurement.get_metric(metric))
                 
    #calculate stat and add to statistics list if needed
    for metric in metrics:
        for stat in stats:
            if metric_dict[metric] and not new_statistic.metric_stat_exists(metric, stat):
                value = stats_dict[stat](metric_dict[metric])
                new_statistic.add_statistic({'metric': metric, 'stat': stat, 'value': value})
                
    #add Statistics object to store if statistics list is not empty
    if new_statistic.statistics:
        stats_store.append(new_statistic)
    return new_statistic.statistics

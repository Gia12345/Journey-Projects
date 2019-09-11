
class Statistics:

    def __init__(self, from_datetime, to_datetime, statistics=[]):
        self.from_datetime = from_datetime
        self.to_datetime = to_datetime
        #statistics variable is a list of dictionaries and each dictionary has a metric, stat, and value
        self.statistics = statistics

    def add_statistic(self, stat_dict):
        self.statistics.append(stat_dict)
    
    def metric_stat_exists(self, metric, stat):
        for s in self.statistics:
            if s['metric'] == metric and s['stat'] == stat:
                return True
        return False

  

from flask import request, jsonify
from flask.views import MethodView
from werkzeug.exceptions import abort
from weathertracker.stats import get_stats
from weathertracker.utils.conversion import (
    convert_to_datetime,
    DatetimeConversionException,
)
from .validation import get_metric_list, get_stats_list, create_response

stats_set = set(get_stats_list().keys())
metrics_set = set(get_metric_list())

class StatsAPI(MethodView):
    # features/02-stats/01-get-stats.feature
    def get(self):

        stats = request.args.getlist("stat")
        metrics = request.args.getlist("metric")
        from_datetime = request.args.get("fromDateTime")
        to_datetime = request.args.get("toDateTime")

        # Validate query params are provided
        if any(
            [
                len(stats) == 0,
                len(metrics) == 0,
                from_datetime is None,
                to_datetime is None
            ]):
            return create_response(400, body={'message':'Invalid query parameters'})
        #validate query params are subsets of valid params
        if not set(stats)<=stats_set or not set(metrics)<=metrics_set:
            return create_response(400, body={'message':'Invalid stats or metrics'})
                
        try:
            from_datetime = convert_to_datetime(from_datetime)
            to_datetime = convert_to_datetime(to_datetime)
        except DatetimeConversionException:
            return create_response(400, body={'message':'Invalid dates'})

        stats = get_stats(stats, metrics, from_datetime, to_datetime)
        return jsonify(stats)

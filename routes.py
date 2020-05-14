from flask import jsonify

# html methods
from middleware import hello, bye, message, version, localtime, add_hours_to_localtime, list_methods
# json methods
from middleware import hello2, bye2,  list_methods2, add_hours_to_localtime2, localtime2


def init_api_routes(app):
    if app:
        app.add_url_rule('/api', 'list_routes', list_routes, methods=['GET'], defaults={'app': app})
        app.add_url_rule('/api/list', 'list_methods', list_methods, methods=['GET'], defaults={'app': app})
        app.add_url_rule('/api/list2', 'list_methods2', list_methods2, methods=['GET'], defaults={'app': app})
        app.add_url_rule('/api/hello', 'hello', hello, methods=['GET'])
        app.add_url_rule('/api/hello2', 'hello2', hello2, methods=['GET'])
        app.add_url_rule('/api/bye', 'bye', bye, methods=['GET'])
        app.add_url_rule('/api/bye2', 'bye2', bye2, methods=['GET'])
        app.add_url_rule('/api/localtime', 'localtime', localtime, methods=['GET'])
        app.add_url_rule('/api/localtime2', 'localtime2', localtime2, methods=['GET'])
        app.add_url_rule('/api/futuretime', 'add_hours_to_localtime', add_hours_to_localtime, methods=['POST'])
        app.add_url_rule('/api/futuretime2', 'add_hours_to_localtime2', add_hours_to_localtime2, methods=['POST'])
        app.add_url_rule('/api/message', 'message', message, methods=['GET'])
        app.add_url_rule('/api/version', 'version', version, methods=['GET'])


def list_routes(app):
    result = []
    for rt in app.url_map.iter_rules():
        result.append({
            'methods': list(rt.methods),
            'route': str(rt)
        })
    return jsonify({'routes': result, 'total': len(result)})

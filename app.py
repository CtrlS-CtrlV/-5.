from flask import Flask, jsonify, request
from config import config_by_name


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    register_routes(app)
    return app


def register_routes(app):

    @app.route('/')
    def index():
        return """
        <h1>Flask App</h1>
        <a href="/about">About</a><br>
        <a href="/api/info">API</a>
        """

    @app.route('/about')
    def about():
        return "<h1>Flask проект</h1>"

    @app.route('/api/info')
    def api_info():
        routes = [str(r) for r in app.url_map.iter_rules()]
        return jsonify({
            "framework": "Flask",
            "debug": app.debug,
            "routes": routes
        })

    @app.route('/greet')
    @app.route('/greet/<name>')
    def greet(name=None):
        if not name:
            name = request.args.get('name', 'Гість')
        return f"<h1>Привіт, {name}!</h1>"


if __name__ == '__main__':
    app = create_app('development')
    app.run(port=5000, debug=True)

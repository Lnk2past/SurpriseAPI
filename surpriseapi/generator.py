import argparse
import random
from flask import Flask
from flask_restplus import Resource, Api
import surpriseapi.utilities.namegenerator as namegenerator


def get_operation():
    operations = ['get', 'put', 'post', 'delete']
    r = random.SystemRandom()
    return r.choice(operations)


def get_endpoint():
    n = namegenerator.get_random_name()
    return f'/{n}'


def parse_inputs():
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument('--endpoint-count', default=10)
    return parser.parse_args()


def main():
    inputs = parse_inputs()
    app = Flask(__name__)
    api = Api(app)
    for i in range(inputs.endpoint_count):
        n = get_endpoint()
        supers = (Resource,)
        attrs = {get_operation(): lambda: None}
        e = api.route(n)(type(n, supers, attrs))
    app.run(debug=True)


if __name__ == '__main__':
    main()

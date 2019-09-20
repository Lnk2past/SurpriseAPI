import argparse
import random
from flask import Flask
from flask_restplus import Resource, Api
import surpriseapi.utilities.namegenerator as namegenerator


def get_operation():
    operations = ['get', 'put', 'post', 'delete']
    r = random.SystemRandom()
    return r.choice(operations)


def get_endpoint(path_probability, path_input_probability):
    n = f'/{namegenerator.get_random_name()}'
    r = random.SystemRandom().random()
    while r > path_probability:
        if r > path_input_probability:
            n += f'/<{namegenerator.get_random_left()}>'
        else:
            n += f'/{namegenerator.get_random_right()}'
        r = random.SystemRandom().random()
    return n


def parse_inputs():
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument('--endpoint-count', default=10)
    parser.add_argument('--path-probability', default=0.60)
    parser.add_argument('--path-input-probability', default=0.80)
    
    return parser.parse_args()


def main():
    inputs = parse_inputs()
    app = Flask(__name__)
    api = Api(app)
    for i in range(inputs.endpoint_count):
        n = get_endpoint(inputs.path_probability, inputs.path_input_probability)
        supers = (Resource,)
        attrs = {get_operation(): lambda: None}
        e = api.route(n)(type(n, supers, attrs))
    app.run(debug=True)


if __name__ == '__main__':
    main()

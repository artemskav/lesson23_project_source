import os
from werkzeug.exceptions import BadRequest
from flask import Flask, request, abort
from utils import solution_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data/apache_logs.txt")


@app.route("/perform_query/", methods=['GET', 'POST'])
def perform_query():
    try:
        cmd_1 = request.args.get('cmd1')
        value_1 = request.args.get('value1')
        cmd_2 = request.args.get('cmd2')
        value_2 = request.args.get('value2')
    except KeyError:
        raise BadRequest()

    if not (cmd_1 and value_1):
        abort(400)

    if not os.path.exists(DATA_DIR):
        return abort(400, 'Wrong filepath')

    with open(DATA_DIR, 'r') as file:
        res = solution_query(cmd_1, value_1, file)
        if cmd_2 and value_2:
            res = solution_query(cmd_2, value_2, res)
        res = "\n".join(res)

    return app.response_class(res, content_type="text/plain")

if __name__ == "__main__":
    app.run(debug=True)

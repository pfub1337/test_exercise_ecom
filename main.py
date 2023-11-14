from tinydb import TinyDB, Query
from flask import Flask, jsonify, request
import re


app = Flask(__name__)
db = TinyDB(f"{__name__.strip('_')}.json")
Form = Query()


DATA_TYPES = ['date', 'email', 'phone', 'text']


def get_data_type(value):
    if re.fullmatch(r'^[0-9]{4}-[0-1][0-9]-[0-3][0-9]$', value):
        date = value.split('-')
        if int(date[1]) <= 7:
            if int(date[1]) % 2 == 1 and int(date[2]) <= 31:
                return 'date'
            elif int(date[0]) % 4 != 0 and int(date[1]) == 2 and int(date[2]) <= 28:
                return 'date'
            elif int(date[0]) % 4 == 0 and int(date[1]) == 2 and int(date[2]) <= 29:
                return 'date'
            elif int(date[1]) % 2 == 0 and int(date[2]) <= 30:
                return 'date'
        elif int(date[1] > 7) and int(date[1]) <= 12:
            if int(date[1]) % 2 == 1 and int(date[2]) <= 30:
                return 'date'
            elif int(date[1]) % 2 == 0 and int(date[2]) <= 31:
                return 'date'
    if re.fullmatch(r'^[0-3][0-9].[0-1][0-9].[0-9]{4}$', value):
        date = value.split('.')
        if int(date[1]) <= 7:
            if int(date[1]) % 2 == 1 and int(date[0]) <= 31:
                return 'date'
            elif int(date[2]) % 4 != 0 and int(date[1]) == 2 and int(date[0]) <= 28:
                return 'date'
            elif int(date[2]) % 4 == 0 and int(date[1]) == 2 and int(date[0]) <= 29:
                return 'date'
            elif int(date[1]) % 2 == 0 and int(date[0]) <= 30:
                return 'date'
        elif int(date[1] > 7) and int(date[1]) <= 12:
            if int(date[1]) % 2 == 1 and int(date[0]) <= 30:
                return 'date'
            elif int(date[1]) % 2 == 0 and int(date[0]) <= 31:
                return 'date'
    if re.fullmatch(r'^\+7\s[0-9]{3}\s[0-9]{3}\s[0-9]{2}\s[0-9]{2}$', value):
        return 'phone'
    if re.fullmatch(r'^[a-zA-Z0-9.\+-_]{1,}@[a-zA-Z0-9.]{1,}$', value):
        return 'email'
    return 'text'


def search(data, response):
    res = []
    db_types = []
    response_types = [(k, get_data_type(v)) for k, v in response.items()]
    fields = list(response.keys())
    for row in data:
        if set(row.keys()).intersection(fields) == set(fields):
            db_types = [(k, v) for k, v in row.items() if k in fields]
            if response_types == db_types:
                res.append({"name": row["name"]})
            # types = [(k, v) for k, v in row.items() if k in fields]
    if not res:
        return {k: v for k, v in response_types}
    return res


@app.route('/create_form', methods=['POST'])
def create_form():
    if "name" in request.form.keys():
        for val in request.form:
            if val == 'name':
                continue
            if request.form[val] not in DATA_TYPES:
                return 'Wrong POST data'
        db.insert(request.form)
        return "data was inserted"
    return 'Wrong POST data'


@app.route('/get_form', methods=['POST'])
def get_form():
    args = []

    if not request.form:
        return "No data in request"
    
    for val in request.form:
        args.append(val)
    
    data = db.all()
    res = search(data, request.form)
    return res


if __name__ == "__main__":
    app.run()
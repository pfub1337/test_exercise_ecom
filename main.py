from tinydb import TinyDB, Query, where
from flask import Flask, jsonify, request


app = Flask(__name__)
db = TinyDB(f"{__name__}.json")
Form = Query()

DATA_TYPES = ['date', 'email', 'phone', 'text']


@app.route('/create_form', methods=['POST'])
def handler():
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
    for val in request.form:
        print(val)
    return "Hello! Watch console log for more information"




# def main():
#     db_name = "forms.json"
#     db = TinyDB(db_name)
#     db.insert({'type': 'peach', 'count': 3})


# if __name__ == "__main__":
#     main()
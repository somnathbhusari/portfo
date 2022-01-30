from flask import Flask, redirect, render_template, request
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def main(page_name):
    return render_template(page_name)


def storing_data(data):
    with open('database.txt', mode='a') as database:
        email = data['Email']
        subject = data['Subject']
        message = data['Message']
        file = database.write(
            f'\nEmail:-{email}, Subject:-{subject}, Message:-{message}')


def data_storing_csv_file(data):
    with open('database.csv', mode='a', newline='') as csv_file:
        email = data['Email']
        subject = data['Subject']
        message = data['Message']
        csv_writer = csv.writer(csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        storing_data(data)
        data_storing_csv_file(data)
        return redirect('/submitted_form.html')
    else:
        return 'Error..!'

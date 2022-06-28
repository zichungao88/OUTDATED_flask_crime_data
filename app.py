import pandas, os
from flask import Flask, render_template

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

data_file_crime = pandas.read_csv('howard-daily-crime-bulletin (1).csv')
publish_date = data_file_crime['publish_date']
category = data_file_crime['category']
city = data_file_crime['city']
zip_code = data_file_crime['zip_code']
street = data_file_crime['street']
crime_date = data_file_crime['crime_date']
crime_time = data_file_crime['crime_time']
add_notes = data_file_crime['add_notes']
data_array = []

for i in range(len(data_file_crime)):
    record = []
    record.append(publish_date[i])
    record.append(category[i])
    record.append(city[i])
    record.append(zip_code[i])
    record.append(street[i])
    record.append(crime_date[i])
    record.append(crime_time[i])
    record.append(add_notes[i])

    # append record to data_array (array of records)
    data_array.append(record)

headings = ('publish_date', 'category', 'city', 'zip_code', 'street', 'crime_date', 'crime_time', 'add_notes')


@app.route('/')
def table():
    return render_template('table.html', headings=headings, data=data_array)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/index/')
def index():
    secret_key = app.config.get("SECRET_KEY")
    return f"The configured secret key is {secret_key}."


if __name__ == '__main__':
    app.run(debug=True)

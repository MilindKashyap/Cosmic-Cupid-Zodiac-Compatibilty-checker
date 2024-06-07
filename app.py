import csv
from flask import Flask, render_template , request 
app = Flask(__name__)

# Read the dataset from the CSV file
def read_dataset():
    dataset = []
    with open('zoDATA.csv', 'r', newline='') as file:  # Replace 'zodiac_dataset.csv' with 'zoDATA.csv'
        reader = csv.DictReader(file)
        for row in reader:
            dataset.append(row)
    return dataset

# Calculate compatibility score based on zodiac signs
def calculate_compatibility(user_zodiac, partner_zodiac, dataset):
    compatibility_score = 0
    for row in dataset:
        if row['Zodiac Sign'] == user_zodiac:
            partner_zodiac = row['Compatible Signs'].split(', ')
            compatibility_score=row['Compatibility Score']
            break
    return compatibility_score


@app.route('/')
def home():
    return render_template('main.html')
    
@app.route('/test')
def test():
    return render_template("test.html")

from flask import request, render_template

@app.route('/submit', methods=['POST'])
def submit():
    dataset = read_dataset()  # Read the dataset
    your_zodiac = request.form['zodiac']  # Get user's zodiac sign from the form
    partner_zodiac = request.form['partner_zodiac']  # Get partner's zodiac sign from the form

    compatibility_score = calculate_compatibility(your_zodiac, partner_zodiac, dataset)  # Calculate compatibility score
    
    # Render the result template with the obtained compatibility score
    return render_template('result.html', 
                           your_zodiac=your_zodiac, 
                           partner_zodiac=partner_zodiac,
                           compatibility_score=compatibility_score)




@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')


if __name__ =="__main__":
    app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:x>/<int:y>')
def BMI(x, y):
    BMI = x / ((y / 100)*(y / 100))
    print(BMI)
    if BMI < 16:
        return "Severely Underweight"
    elif BMI < 18.5:
        return "Underweight"
    elif BMI < 25:
        return "Normal"
    elif BMI < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == '__main__':
  app.run(debug=True)

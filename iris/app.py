from flask import Flask, render_template, request
import main

app = Flask(__name__)

@app.route("/")

def hello():
    return render_template("index.html")

@app.route("/submit-page", methods = ["POST"])
def submit():
    # take date from html page to python file
    if request.method == "POST":
        sepal_length = request.form["sepallength"]
        sepal_width = request.form["sepalwidth"]
        petal_length = request.form["petallength"]
        petal_width = request.form["petalwidth"]

        data_entered = "Voici les données que vous avez entrées: " + sepal_length + ", " + sepal_width + ", " + petal_length + ", " + petal_width + ". Ce qui correspond a la variEtE : "

        class_pred = main.iris_prediction(int(sepal_length), 
                                          int(sepal_width), 
                                          int(petal_length), 
                                          int(petal_width)
                                          )
        
    # take date from python file to html    
    #return render_template("submit-page.html", sl=sepal_length, sw=sepal_width, pl=petal_length, pw=petal_width)
    return render_template("submit-page.html", user_request = data_entered, pred = class_pred)
    

if __name__== "__main__":
    app.run(debug=True)
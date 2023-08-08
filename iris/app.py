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

        # data_entered = "Voici les données que vous avez entrées: " + sepal_length + ", " + sepal_width + ", " + petal_length + ", " + petal_width + ". Ce qui correspond a la variEtE : "

        class_pred = main.iris_prediction(float(sepal_length), 
                                          float(sepal_width), 
                                          float(petal_length), 
                                          float(petal_width)
                                          )
        
        pred_result = "Voici dans l'ordre les données que vous avez entrées: " + sepal_length + ", " + sepal_width + ", " + petal_length + ", " + petal_width + ". Ce qui correspond a la variété : " + class_pred

        
    # take date from python file to html    
    #return render_template("submit-page.html", sl=sepal_length, sw=sepal_width, pl=petal_length, pw=petal_width)
    return render_template("submit-page.html", pred = pred_result)
    

if __name__== "__main__":
    app.run(debug=True)
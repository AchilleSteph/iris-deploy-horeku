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



        class_pred = main.iris_prediction(float(sepal_length), 
                                          float(sepal_width), 
                                          float(petal_length), 
                                          float(petal_width)
                                          )
        
        user_request = "Voici dans l'ordre les données que vous avez entrées: " + sepal_length + ", " + sepal_width + ", " + petal_length + ", " + petal_width  
        pred_result = "Ce qui correspond a la variété : " + class_pred

      
      
    
    return render_template("submit-page.html", request = user_request, pred = pred_result)
    

if __name__== "__main__":
    app.run(debug=True)
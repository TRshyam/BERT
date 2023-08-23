from flask import Flask,render_template,request

app= Flask(__name__)

# @app.route("/",methods=['POST','GET'])
# def index():
#     message=request.form["message"]

#     return render_template('index.html')

@app.route("/", methods=['POST', 'GET'])
def index():
    message = "  "  # Initialize the message variable

    if request.method == 'POST':
        message = request.form["message"]  # Get the message from the form
    return render_template('index.html', message=message)
# @app.route("")

if __name__ =="__main__":
    app.run(host='0.0.0.0',debug=True)
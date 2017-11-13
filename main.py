from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] =  True


form = """

<!DOCTYPE html>

<html>
<head>
        <style>
            form {
                background-color: #eee
                ;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>


    <body>
      <!-- create your form here -->

    <form action="/encrypt" method="POST">

    <label for="rotate"> Rotate by:</label>
    <!--<label for="text"> Enter text:</label> -->

				
	<input id="rotate" type="text" name="rot" value=0 />
    <label = "asdf">
    <textarea id="text" name="text"></textarea>
    </label>
			
	<input type="submit" />
			
		</form>


    </body>

"""
 
@app.route("/")
def index():
        return form

#@app.route("/hello", methods=['POST'])
#def hello():
#	rot = request.form['rot']
	
#	return '<h1> Hello, ' + rot + '</h1>' 



@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    message = rotate_string(text, rot)
    message = '<h1>'+ message + '</h1>'
    return message

app.run()
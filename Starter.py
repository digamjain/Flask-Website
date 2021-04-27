from flask import Flask
app = Flask(__name__) #Creating a flask instance referring to local file( __name__ )

#HOMEPAGE or index page
@app.route('/') #Decorator to display something on '/' route
#Function hello_world
def hello_world():
    return ('Hello World') #Function to print hello world on the webpage

#Testing HTML tags within returning strings
@app.route('/html_test') #Decorator to display Hello World under /html_test route
#Function html_tag
def html_tag():
    return('<h1>Hello World</h1>') #Function to print hello world using h1 HTML tag

#Dynamic routes
@app.route('/test/<name>') #Decorator to display txt under '/test/<name>' route which is dynamic in nature
#Function name
def name_chk(name):
    return(f"test page for {name}")

#test1/<name>
@app.route("/test1/<name>/") #Decorator to display txt under '/test1/<name>' route which is dynamic in nature
#Function to check acess to some special users
def name_test(name):
	names_list = ['YourName', 'Admin', 'MyName'] #All the names in the list will be checked
	if name in names_list:
		return (f'<title> Welcome {name} </title> \
			       <h1> Good Day Mr.{name} </h1>') #If URL route in list display this
	else:
		return ('<h1> Unidentified login attempt </h1>') #Else display this

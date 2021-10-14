from flask import (
    Flask, 
    render_template, 
    request, 
    session
)
 


class User:
    def __init__(self, id, username,password):
        self.id = id
        self.username = username
        self.password = password
    def __repr__(self):
        return f'<User: {self.username}>'

users = [] 
users.append(User(id =1, username = 'Aybike', password = 'passwordaybike'))

print(users)

app = Flask(__name__)  

@app.route("/")
@app.route("/home")
def home():
    return render_template ('home.html')

@app.route("/login")
def login():
    
    return render_template ('login.html')

@app.route("/signup")
def signup():
    return render_template ('signup.html')

if __name__ == "__main__":
    app.run(debug=True)

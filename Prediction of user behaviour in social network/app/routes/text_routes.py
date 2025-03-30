from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.services.behavior_service import analyze_text_behavior

text_bp = Blueprint('text', __name__)

@text_bp.route('/sen')
def sentence():
    return render_template('sentence.html')

@text_bp.route('/pre', methods=["POST"])
def pre():
    text = request.form['text']
    output = analyze_text_behavior(text)
    return render_template("pre.html", output=output)
from flask import Blueprint, render_template, request, redirect, url_for
from app.services.sentiment_service import analyze_paragraph

para_bp = Blueprint('para', __name__)

@para_bp.route('/para')
def para():
    return render_template('para.html')

@para_bp.route('/paragraph_sentiment', methods=['POST'])
def paragraph_sentiment():
    paragraph = request.form['paragraph']
    result = analyze_paragraph(paragraph)
    return render_template('paragraph_sentiment.html', **result)
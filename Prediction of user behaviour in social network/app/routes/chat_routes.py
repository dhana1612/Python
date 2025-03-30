from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.services.analysis_service import analyze_chat_file

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/Frontpage')
def home():
    if 'username' not in session:
        return redirect(url_for('auth.index'))
    return render_template('Frontpage.html')

@chat_bp.route('/home')
@chat_bp.route('/doc')
def document():
    return render_template('home.html')

@chat_bp.route('/analyze', methods=['POST'])
def analyze():
    try:
        file = request.files['file']
        results = analyze_chat_file(file)
        return render_template('result.html', **results)
    except Exception as e:
        flash("Analysis failed", "error")
        return redirect(url_for('chat.home'))
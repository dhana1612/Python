from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.services.audio_service import transcribe_audio
from app.services.behavior_service import analyze_text_behavior

voice_bp = Blueprint('voice', __name__)

@voice_bp.route('/voice')
def voice_input():
    return render_template('voice_input.html')

@voice_bp.route('/voicepre', methods=["POST"])
def voicepre():
    try:
        text = request.form.get('text')
        if not text:
            text = transcribe_audio()
            if not text:
                flash("Could not recognize speech", "error")
                return redirect(url_for('voice.voice_input'))
        
        output = analyze_text_behavior(text)
        return render_template("voicepre.html", output=output)
    
    except Exception as e:
        flash("Voice processing failed", "error")
        return redirect(url_for('voice.voice_input'))
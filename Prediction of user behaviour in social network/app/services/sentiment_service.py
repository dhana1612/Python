from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator
from functools import lru_cache

@lru_cache(maxsize=1)
def get_sentiment_analyzer():
    return SentimentIntensityAnalyzer()

@lru_cache(maxsize=1)
def get_translator():
    return Translator()

def get_sentiment_label(text):
    analyzer = get_sentiment_analyzer()
    scores = analyzer.polarity_scores(text)
    if scores['compound'] >= 0.05:
        return "positive"
    elif scores['compound'] <= -0.05:
        return "negative"
    return "neutral"

def analyze_paragraph(paragraph):
    translator = get_translator()
    translated = translator.translate(paragraph, dest='en').text
    
    analyzer = get_sentiment_analyzer()
    scores = analyzer.polarity_scores(translated)
    
    return {
        'paragraph': paragraph,
        'translated_paragraph': translated,
        'label': 'Positive' if scores['compound'] > 0 else 'Negative' if scores['compound'] < 0 else 'Neutral',
        'score': scores['compound']
    }
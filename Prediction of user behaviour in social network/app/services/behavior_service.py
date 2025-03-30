from app.services.sentiment_service import get_sentiment_label
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import pandas as pd
import joblib
import os

def analyze_text_behavior(text):
    behavior_label = predict_behavior_label(text)
    sentiment_label = get_sentiment_label(text)
    
    # All original conditions preserved
    if behavior_label == "Crime":
        if sentiment_label == "positive":
            return "The sentiment is positive and it is labeled as Non-violent."
        else:
            return "The sentiment is negative and it is labeled as Crime."
    
    elif behavior_label == "Short-temper":
        if sentiment_label == "positive":
            return "The sentiment is positive and it is labeled as Calm"
        else:
            return "The sentiment is negative and it is labeled as short-temper."
    
    elif Behaviour_label == "Appreciation":
        if sentiment_label == "positive":
            output = "The sentiment in the sentence is classified as positive and it is labeled as Appreciation."
        else:
            output = "The sentiment in the sentence is classified as negative and it is labeled as Depreciation"
            
    elif Behaviour_label == "Enthusiasm":
        if sentiment_label == "positive":
            output = "The Sentiment in the sentence is classified as positive and it labeled as Enthusiasm"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as Unenthusiasm"
    
    elif Behaviour_label == "Optimistic":
        if sentiment_label == "positive":
            output = "The Sentiment in the sentence is classified as positive and it labeled as Optimistic"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as Pesimestic"

    elif Behaviour_label == "Caring":
        if sentiment_label == "positive":
            output = "The Sentiment in the sentence is classified as positive and it labeled as Caring"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as Careless"

    elif Behaviour_label == "Relief":
        if sentiment_label == "positive":
            output = "The Sentiment in the sentence is classified as positive and it labeled as Relief"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as Discomfort"

    elif Behaviour_label == "Depressed":
        if sentiment_label == "positive":
            output = "The Sentiment in the sentence is classified as positive and it labeled as Happy"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as Depressed"

    elif Behaviour_label == "Disgust":
        if sentiment_label == "positive":
            output = "The Sentiment in the sentence is classified as positive and it labeled as Attraction"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as  Disgust"


    elif Behaviour_label == "Introvert":
        if sentiment_label == "positive":
           output = "The Sentiment in the sentence is classified as positive and it labeled as Extrovert"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as  introver"


    elif Behaviour_label == "Clever":
        if sentiment_label == "positive":
            output = "The Sentiment in the sentence is classified as positive and it labeled as Clever"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as Foolish"

    elif Behaviour_label == "Friendly":
        if sentiment_label == "positive":
            output = "The Sentiment in the sentence is classified as positive and it labeled as Friendly"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as Unfriendly"

    elif Behaviour_label == "Helpful":
        if sentiment_label == "positive":
            output = "The Sentiment in the sentence is classified as positive and it labeled as Helpful"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as Unhelpful"

    elif Behaviour_label == "mental illness":
        if sentiment_label == "positive":
            output = "The Sentiment in the sentence is classified as postive and it labeled as Stable"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as mental illness"

    elif Behaviour_label == "Confident":
        if sentiment_label == "positive":
            output = "The Sentiment in the sentence is classified as positive and it labeled as Confident"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as Unconfident"

    elif Behaviour_label == "selfish":
        if sentiment_label == "positive":
            output = "The Sentiment in the sentence is classified as positive and it labeled as Unselfish"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as selfish"

    elif Behaviour_label == "Honest":
        if sentiment_label == "positive":
            output = "The Sentiment in the sentence is classified as positive and it labeled as Honest"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as Dishonest"


    elif Behaviour_label == "laziness ":
        if sentiment_label == "positive":
            output = "The Sentiment in the sentence is classified as positive and it labeled as Active"
        else:
            output = "The Sentiment in the sentence is classified as negative and it labeled as  laziness"
    
    elif behavior_label == "Relaxation":
        if sentiment_label == "positive":
            return "The sentiment is positive and it labeled as Relaxation"
        else:
            return "The sentiment is negative and it labeled as Discomfort"
    
    return f"The sentiment is {sentiment_label} and the behavior is {behavior_label}"

def predict_behavior_label(text):
    # Your original behavior prediction logic
    ...
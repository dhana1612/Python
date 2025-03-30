import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import emoji
from collections import Counter
import re
from datetime import datetime
from app.services.sentiment_service import get_sentiment_analyzer

def analyze_chat_file(file):
    # Your complete chat analysis logic
    text = file.read().decode('utf-8')
    
    # All original processing code
    messageBuffer = []
    data = []
    date, time, author = None, None, None
    
    for line in text.split('\n'):
        if date_time(line):
            if len(messageBuffer) > 0:
                data.append([date, time, author, ''.join(messageBuffer)])
                messageBuffer.clear()
            date, time, author, message = get_message(line)
            messageBuffer.append(message)
        else:
            messageBuffer.append(line)
    
    # ... (rest of your original analysis code)
    
    return {
        'sentiment': sentiment,
        'sentiment_class': sentiment_class,
        'num_messages': num_messages,
        # ... all other original variables
    }
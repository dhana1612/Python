import re
from datetime import datetime

def date_time(s):
    pattern = r'^([0-9]+)(\/)([0-9]+)(\/)([0-9]+), ([0-9]+):([0-9]+)[ ]?(AM|PM|am|pm)? -'
    return bool(re.match(pattern, s))

def find_contact(s):
    return len(s.split(":")) == 2

def get_message(line):
    split_line = line.split(' - ')
    datetime = split_line[0]
    date, time = datetime.split(', ')
    message = " ".join(split_line[1:])
    
    if find_contact(message):
        split_message = message.split(": ")
        author = split_message[0]
        message = split_message[1]
    else:
        author = None
    return date, time, author, message
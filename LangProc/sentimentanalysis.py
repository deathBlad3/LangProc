from textblob import TextBlob

speech = TextBlob('Sunday is a great morning to program.. at 5 AM.')
print speech,speech.sentiment,str(speech.sentiment.polarity).encode('ascii'),str(speech.sentiment.subjectivity).encode('ascii')


class SentimentAnalysis:
    def __init__(self):
        pass

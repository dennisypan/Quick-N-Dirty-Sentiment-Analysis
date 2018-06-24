import pandas as pd
from textblob import TextBlob

#read data from a csv file to a Pandas dataframe, save it as "dataset"
dataset = pd.read_csv('Comments_SushiMaru.csv')

BuzArry = []
CommentArry = []
RatingArry = []
UrlArry = []
sentimentsScoreArry = []
sentimentsTextArry = []

for x in range(0, len(dataset)):
    BuzArry.append(dataset.iloc[x]["BUSINESS_NAME"])
    CommentArry.append(dataset.iloc[x]["COMMENT"])
    RatingArry.append(dataset.iloc[x]["RATING_STARS"])
    UrlArry.append(dataset.iloc[x]["URL"])

	
#Apply "TextBlob" on each comment string, and extract the sentiment polarity scroe of that comment.      
for i in range(0, len(dataset)):
    temps = TextBlob(dataset.iloc[i]["COMMENT"])
    sentimentsScoreArry.append(temps.sentiment.polarity)

for s in range(0, len(sentimentsScoreArry)):
    if(sentimentsScoreArry[s] == 0):
        sentimentsTextArry.append("Neutral")
        
    if(sentimentsScoreArry[s] > 0):
        sentimentsTextArry.append("Positive")
        
    if(sentimentsScoreArry[s] < 0):
        sentimentsTextArry.append("Negative")                   
		
		
#Merge 3 arrays into one Pandas Data Frame
df1 = pd.DataFrame({'Business':BuzArry, 'Comments':CommentArry, 'Rating':RatingArry, 'URL':UrlArry, 'Sentiment Score':sentimentsScoreArry, 'Sentiment Label':sentimentsTextArry})

df1.to_csv('sentiment_on_business.csv')

	
#average sentiment score
df1['Sentiment Score'].mean()

Label = ""

if(df1['Sentiment Score'].mean() > 0):
    Label = "Positive"
    
if(df1['Sentiment Score'].mean() == 0):
    Label = "Neutral"
    
if(df1['Sentiment Score'].mean() < 0):
    Label = "Negative"

#Display overall sentiment of the business
print(df1.iloc[0]["Business"] + " SENTIMENT: " + str(df1['Sentiment Score'].mean()) + " | " + Label)    
		

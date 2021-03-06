# Quick-N-Dirty-Sentiment-Analysis
<b>Introduction</b>

Suppose you got a CSV file with rows of distinct comments and 5-stars ratings on a business (e.g. a restaurant from Yelp).  This Python tool/program will process data from this CSV input file to (1) produce an output CSV file giving each row a "Sentiment Label" and a "Sentiment Score", and (2) a statement on Command Prompt (Windows) describing the overall sentiment (Positive, Neutral, Negative) of the business.

The main engine of this tool is the <b>TextBlob</b> Python library.  In a nutshell, to know the sentiment of a string (e.g. "I love the food in Sushi Maru"), use this string as the parameter when creating a TextBlob object (e.g. temps = TextBlob("I love the food in Sushi Maru")), and extract the sentiment information from this newly created TextBlob object (e.g. score = temps.sentiment.polarity).  If the input CSV file contains 100 different comments on a business, basically we use a for loop to repeat the above process 100X so all comment rows are processed, so we can know the sentiments of all these comments. 

Note the extracted sentiment score from TextBlob is a floating number between -1 and 1.  If this score is > 0, that means the string is a "Positive" statement.  If this score is 0, that means the string is a "Neutral" statement.  If this score is < 0, the string is a "Negative" statement. 

________________________________________

<b>To run this tool, do the following:</b>

1) Ensure you have Python 3 installed, as well as having "Pandas" and "Textblob" dependencies installed.  If the 2 dependencies are missing on your computer, on Command Prompt (Windows) run "pip3 install pandas" followed by "pip3 install textblob".

2) Download the 2 files (SA1.py and Comments_SushiMaru.csv) and place them in the same folder.  

3) One way to run this tool is to double-click "SA1.py" Python file, which will produce an output CSV file "sentiment_on_business.csv" in which each row has a "Sentiment Label" and a "Sentiment Score."  The output CSV file will appear in the same directory that contains "SA1.py" python file.

4) Another way to run this tool is through the Command Prompt.  So you first "cd" to the directory containing "SA1.py" file, and run the command "py SA1.py" in the Command Prompt.  After doing so, (1) this will produce an output CSV file "sentiment_on_business.csv" in which each row has a "Sentiment Label" and a "Sentiment Score", and (2) show a statement on Command Prompt describing the overall sentiment (Positive, Neutral, Negative) of the business (e.g. Sushi Maru SENTIMENT: 0.2543902403701638 | Positive).  The output CSV file will appear in the same directory that contains "SA1.py" python file.

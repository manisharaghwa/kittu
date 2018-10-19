#Use the "https://api.forismatic.com/api/1.0/" api to get random quotes using the correct endpoints.
import requests
response=requests.get("http://api.forsmatic.com/api/1.0/?method=getQuote&lang=en&format=json&json=?")
print(response.status_code)
b'?({"quoteText":"fears are nothing more than a state of mind ","QuoteAuthor":"neoplin hill","senderName":"","senderlink":""})'

import feedparser
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

RSS_FEED = {"bbc": "http://feeds.bbci.co.uk/news/rss.xml",
        "fox": "http://feeds.foxnews.com/foxnews/latest",
        "cnn": "http://rss.cnn.com/rss/edition.rss",
        }

@app.route("/")
@app.route("/<pub>")
def get_news(pub="bbc"):
    query = request.args.get("pub")
    if not query or query.lower() not in RSS_FEED:
        pub =  "bbc"
    else:
        pub = query.lower()
    feed = feedparser.parse(RSS_FEED[pub])
    return render_template("home.html",
                           articles=feed["entries"]
                          )

if __name__ == "__main__":
	app.run(debug=True)

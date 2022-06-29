from flask import Blueprint, render_template
from prettytable import PrettyTable
import requests
import html

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route('/test' , methods=['POST'])
def my_link():
    output = requests.get_json()
    return output.data

@views.route("/data")
def get_data():
    diff_table = PrettyTable(['Title', 'Link', 'Date', 'Source'])
    result = requests.get("https://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=rneTUg5zvyLj56LTP9SR5dTGSAwIwHX3")
    res = result.json()
    data = res['results']
    a = 'blablablas'

    for count, commit in enumerate(data, 1):
        diff_table.add_row([
            
            commit['title'],
            '<input type="hidden" id="v'+str(count)+'" value="'+commit['abstract']+'"><button type="submit" id="b'+str(count)+'" onclick="func('+str(count)+')">Read More</button>',
            #'<input type="hidden" id="v'+str(count)+'" value="'+commit['abstract']+'"><button type="submit" id="b'+str(count)+'">Read More</button>',
            commit['published_date'],
            commit['source']
        ])

    # --- after loop ---

    text = diff_table.get_html_string(format=True)
    text = html.unescape(text)

    res = text
    
    return render_template("index.html", tbl=res)
''' 
request - used for browser communication. GET/POST methods
redirect - re-direct the URL 
escape - used for formatting HTML tags
'''
from flask import Flask, render_template, request, redirect, escape
from vowels import count

app = Flask(__name__)

"""This funtion accepts the values entered in the entry.HTML 
Posts to the do_search(); that further process the input and renders the output
to the results.html page
"""

@app.route('/count', methods=['POST'])
def do_search() -> str:
    Phrase = request.form['phrase']
    title = "Results Form"
    results = str(count(Phrase))
    log_request (request, results)
    return render_template('results.html',the_phrase = Phrase, the_title=title, the_results = results, )


"""Re-direct default URL to the entry_page function followed by another URL for for the same function  """
@app.route('/')
@app.route('/enter')
def entry_page() -> 'html':
    return render_template('entry.html', the_title = 'Entry Form')


"""a function that creates a log file and logs ceratin values from the request and response"""
def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log','a') as log:
        print(req.form, file =log, end="|")
        print(req.remote_addr, file =log, end="|")
        print(res, file =log, end="|")


app.run(debug=True)
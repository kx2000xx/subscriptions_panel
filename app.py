from flask import Flask, render_template, request, redirect, url_for
import json
import math
app = Flask(__name__)
with open('SUBSCRIBERS.json', 'r') as file:
    subscribers = json.load(file)
@app.route('/')
@app.route('/index.html')
def index():

    if not subscribers:
        message = "لا يوجد مشتركين"
        return render_template('index.html', message=message)
    
    page = request.args.get('page', 1, type=int)
    per_page = 10
    total = len(subscribers)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_subscribers = subscribers[start:end]
    total_pages = math.ceil(total / per_page)

    return render_template('index.html', subscribers=paginated_subscribers, total_pages=total_pages, current_page=page)

@app.route('/add.html')
def display_add():
    return render_template('add.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    userid = request.form.get('userid')  # Get the value of the 'name' field from the form
    name = request.form.get('name')  # Get the value of the 'email' field from the form
    expiry_date = request.form.get("expiry_date")
    newsub = {"userid": userid, "name": name, "expiry_date": expiry_date}
    subscribers.append(newsub)
    with open('SUBSCRIBERS.json', 'w') as file:
        json.dump(subscribers, file, indent=4)
    return redirect(url_for('index'))
    #return f"Received form data: Name - {name}, User ID - {userid}"


if __name__ == '__main__':
    app.run(debug=True)

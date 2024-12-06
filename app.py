from flask import Flask, render_template, request, redirect, url_for
import json
import math
from post import change_role
app = Flask(__name__)
with open('SUBSCRIBERS.json', 'r') as file:
    subscribers = json.load(file)
@app.route('/')
@app.route('/index.html')
def index():
    if not subscribers:
        message = "لا يوجد مشتركين"
        return render_template('index.html', message=message, total_pages=1, current_page=1)
    
    search_query = request.args.get('search', '', type=str)
    page = request.args.get('page', 1, type=int)
    per_page = 10
    total = len(subscribers)
    start = (page - 1) * per_page
    end = start + per_page
    total_pages = math.ceil(total / per_page)
    if search_query:
        filtered_subscribers = [sub for sub in subscribers if search_query.lower() in sub['name'].lower()]
        paginated_subscribers = filtered_subscribers[start:end]
        if len(filtered_subscribers) == 0:
            message = "أسم المستخدم غير موجود"
            return render_template('index.html', message=message, total_pages=1, current_page=1)

        
    else:
        paginated_subscribers = subscribers[start:end]


    return render_template('index.html', subscribers=paginated_subscribers, total_pages=total_pages, current_page=page)

@app.route('/add.html')
def display_add():
    return render_template('add.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    userid = request.form.get('userid')  # Get the value of the 'name' field from the form
    name = request.form.get('name')  # Get the value of the 'email' field from the form
    expiry_date = request.form.get("expiry_date")
    #newsub = {"userid": userid, "name": name, "expiry_date": expiry_date}
    newsub = {"name": name, "expiry_date": expiry_date}
    subscribers.append(newsub)
    try:
        change_role(name, expiry_date, '7')
        with open('SUBSCRIBERS.json', 'w') as file:
            json.dump(subscribers, file, indent=4)
        return redirect(url_for('index'))
    except:
        return "Something went wrong."

if __name__ == '__main__':
    app.run(debug=True)
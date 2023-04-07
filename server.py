from flask import Flask, render_template, request, redirect

app = Flask(__name__)

topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'},
]

@app.route('/')
def index():
    return render_template('index.html', topics=topics)


@app.route('/create/', methods=['GET','POST'])
def create():
    if len(topics) != 0:
        id = topics[-1]['id']
        nextId = id + 1
    else:
        nextId = 1
    if request.method == 'POST': 
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': nextId, 'title': title, 'body': body}
        topics.append(newTopic)
        url = '/read/' + str(nextId) + '/'
        return redirect(url)
    return render_template('create.html', topics=topics, title='create')


@app.route('/read/<int:id>/')
def read(id):
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return render_template('read.html', topics=topics, title=title, body=body, id=id)

@app.route('/update/<int:id>/', methods=['GET','POST'])
def update(id):
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break

    if request.method == 'POST':
        for topic in topics:
            if id == topic['id']:
                topic['title'] = request.form['title']
                topic['body'] = request.form['body']
                break
        url = '/read/' + str(id) + '/'
        return redirect(url)

    return render_template('update.html', topics=topics, title=title, body=body, id=id)
    
@app.route('/delete/<int:id>/', methods=['POST'])
def delete(id):
    for topic in topics:
        if id == topic['id']:
            topics.remove(topic)
            break
    return redirect('/')


app.run(port=5001, debug=False)
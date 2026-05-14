from flask import Flask, render_template, request, redirect

app = Flask(__name__)

books = []

@app.route('/')
def home():
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    books.append(title)
    return redirect('/')

@app.route('/api/books')
def api_books():
    return {"books": books}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
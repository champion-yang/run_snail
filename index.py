from apps import app


@app.route('/')
def check_self():
    return 200, 'ok'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

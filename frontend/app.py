from application import app
from os import getenv

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

from flaskblog import app # imports from __init__.py

if __name__ == '__main__': # if script run directly, and not imported as a module
    app.run(debug=True, host='0.0.0.0')

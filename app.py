from flask import Flask
from supabase_api.api.user_api import user_api

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(user_api)

if __name__ == '__main__':
    app.run(debug=True)

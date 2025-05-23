from flask import Flask
# ...existing imports...
from app.routes.cultural_items import cultural_items_bp

app = Flask(__name__)
# ...existing code...

# Register blueprints
app.register_blueprint(cultural_items_bp)

# ...existing code...
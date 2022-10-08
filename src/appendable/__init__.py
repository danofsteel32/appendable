from quart import Quart, render_template
from .dashboard import dash_bp
from .list import list_bp


__version__ = "0.1.0"

app = Quart(__name__)
app.config.from_prefixed_env()

dash_bp.register_blueprint(list_bp, url_prefix="/list")
app.register_blueprint(dash_bp, url_prefix="/dashboard")


@app.route("/", methods=["GET"])
async def index():
    return await render_template("index.html")

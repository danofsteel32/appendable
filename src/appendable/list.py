from quart import Blueprint, render_template


list_bp = Blueprint("dashboard", __name__)


# TODO list_pop
# TODO list_put


@list_bp.route("/<list_name>", methods=["GET"])
async def index(list_name: str):
    return render_template("list_index.html", list_name=list_name)

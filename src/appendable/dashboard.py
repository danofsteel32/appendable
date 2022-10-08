from quart import Blueprint, render_template


dash_bp = Blueprint("dashboard", __name__)

# TODO create database for app_name if not exists
# TODO get lists and their items from the database
# TODO new_list and delete_list buttons and routes


class ItemList:

    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items


@dash_bp.route("/<app_name>", methods=["GET"])
async def index(app_name: str):
    lists = [
        ItemList(
            "Civs",
            items=[
                "Zululand",
                "Germany",
                "Mongolia",
            ]
        ),
        ItemList(
            "Leaders",
            items=[
                "Shaka",
                "Bismarck",
                "Genghis Khan",
            ]
        ),
    ]
    return await render_template("dash_index.html", app_name=app_name, lists=lists)

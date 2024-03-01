from typing import Any

from flask import Flask, render_template, abort

app: Flask = Flask(__name__)

projects: list[dict[str, Any]] = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://udemy.com",
    },
    {
        "name": "Personal finance tracking app with React",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["react", "javascript"],
        "slug": "personal-finance",
    },
    {
        "name": "REST API Documentation with Postman and Swagger",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["writing"],
        "slug": "api-docs",
    },
]

slug_to_project: dict[str, Any] = {
    project['slug']: project for project in projects
}




@app.route("/")
def home() -> Any:
    return render_template("home.html", projects=projects)


@app.route("/about")
def about() -> Any:
    return render_template("about.html")


@app.route("/contact")
def contact() -> Any:
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug: str) -> Any:
    if slug not in slug_to_project:
        abort(404)
    return render_template(
        f"project_{slug}.html",
        project=slug_to_project[slug]
    )


@app.errorhandler(404)
def page_not_found(error: int) -> Any:
    return render_template("404.html"), 404
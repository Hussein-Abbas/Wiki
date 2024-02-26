from django.shortcuts import render

from . import util

import markdown2 


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title: str):
    """Presenting a page that displays the content of the entry."""

    # Retrieve the content of a page by its title if available.
    if not (page := util.get_entry(title)):

        # If not found: create a 404 error page with its title and content.
        page = f"<h1>404. That's an error</h1> <p>The requested URL /{title} was not found on this server.</p>"
        title = "Error 404 (Not Found)!"

    # Render the requested entry page.
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": markdown2.markdown(page)
    })

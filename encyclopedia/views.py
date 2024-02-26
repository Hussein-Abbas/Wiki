from django.shortcuts import render

from . import util

import markdown2 


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    """Presenting a page that displays the content of the entry."""

    # Retrieve the content of a page by its title if available.
    if page := util.get_entry(title):
        # Render the requested entry page.
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": markdown2.markdown(page)
        })

    # If not found: render 404 error page.
    return render(request, "encyclopedia/404error.html", {
        "title": title
    })

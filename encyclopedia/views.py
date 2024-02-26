from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

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


def search(request):
    """
    Search across all entries.

    Parameters:
    - request: HttpRequest object

    Returns:
    - HttpResponseRedirect: Redirects to the entry page if a matching entry is found.
    - HttpResponse: Renders a page listing entries containing the query as a substring.
    """

    # Get the title of the entry from the request.
    title = request.GET.get("q", "")

    # Check if there is a matching entry.
    if util.get_entry(title):
        # If found, redirect to the entry page.
        return HttpResponseRedirect(reverse("entry", args=[title]))

    # If no matching entry is found, render a page listing entries containing the query as a substring.
    entries = [entry for entry in util.list_entries() if title.lower() in entry.lower()]
    return render(request, "encyclopedia/search.html", {
        "entries": entries,
        "title": title
    })
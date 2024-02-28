from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

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

    # If not found: render the error page.
    return render(request, "encyclopedia/error.html", {
        "error_title": "Error 404 (Not Found)!",
        "details": f"The requested URL /{title} was not found on this server. That's all we know."
    })


def search(request):
    """Search across all entries."""
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


class NewForm(forms.Form):
    title = forms.CharField(label="Title:")
    content = forms.CharField(label="Content:", widget=forms.Textarea)


# Create a new page.
def newpage(request):
    """Creating a new page."""
    # Check if the request method is POST
    if request.method == "POST":
        # Take in the data the user submitted and save it as form.
        form = NewForm(request.POST)
        # Validate the form.
        if form.is_valid():
            # Extract the title and content from the form.
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            # Check if the title already exists.
            if util.get_entry(title):
                # Render the error page if the title already exists.
                return render(request, "encyclopedia/error.html", {
                    "error_title": "Entry already exists!",
                    "details": "Entry's title already exists. Change entry's title to create it."
                })
            else:
                # Save the new entry.
                util.save_entry(title, content)
                # Redirect to the newly created page.
                return HttpResponseRedirect(reverse("entry", args=[title]))
        else:
            # Render the error page if the form is not valid.
            return render(request, "encyclopedia/error.html", {
                "error_title": "Inputs Error",
                "details": "Missing title and/or content"
            })

    # Render the newpage.html template when the method is GET.
    return render(request, "encyclopedia/newpage.html")

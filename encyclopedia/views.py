from django.shortcuts import render, redirect
from markdown2 import markdown
from . import util
from random import randint
import re


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title.strip())
    if content == None:
        return render(request, "encyclopedia/error.html")
    else:
        title = markdown(title)
        content = markdown(content)
    return render(request, "encyclopedia/entry.html", {
        'content': content,
        'title': title
        })

def search(request):
    query = request.GET.get('q')
    entries = util.list_entries()

    if query in entries:
        return redirect("entry", title=query)
    else:
        for entry in entries:
            if re.findall(f"{query}", entry, re.IGNORECASE):
                print(entry)
                return render(request, "encyclopedia/search_results.html", {
                    "entries": util.list_entries()
                    })
        
    


    """
        where is entries coming from line 23
        what format are you getting entries in 
        what parameters do you need to pass to 'results.html"
        how to get in from entries in wiki
    """
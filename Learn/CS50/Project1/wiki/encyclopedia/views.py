from django.forms.widgets import Textarea
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django import forms
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def viewEntry(request, title):
    entry = util.get_entry(title.lower())
    if entry:
        return render(
            request, "encyclopedia/entry.html", {"entry": entry, "title": title}
        )
    else:
        return render(request, "encyclopedia/404.html")


def searchResults(request):
    query = request.GET.get("q")
    entry_list = util.list_entries()

    def filterString(entry):
        if query.lower() in entry.lower():
            return True
        else:
            return False

    if query:
        searched_entry = util.get_entry(query)

        if searched_entry:
            return redirect(reverse("entry", args=[query]))
        else:
            search_results = filter(filterString, entry_list)
            return render(
                request, "encyclopedia/search.html", {"search_results": search_results}
            )


def newPage(request):
    class NewPageForm(forms.Form):
        title = forms.CharField(label="Title", max_length=200)
        content = forms.CharField(widget=forms.Textarea)

        def clean(self):
            cd = self.cleaned_data
            if util.get_entry(cd.get("title")):
                self.add_error("title", "A page by the same name already exists.")
                return cd

    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title):
                return render(request, "encyclopedia/newPage.html", {"form": form})
            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("index"))
    else:
        form = NewPageForm()

    return render(request, "encyclopedia/newPage.html", {"form": form})


def editEntry(request, title):
    entry = util.get_entry(title)

    class EditForm(forms.Form):
        content = forms.CharField(widget=forms.Textarea, initial=entry)

    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return redirect(reverse("entry", args=[title]))
    else:
        form = EditForm
    return render(request, "encyclopedia/editPage.html", {"title": title, "form": form})
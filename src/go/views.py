from typing import Any
from django.forms import model_to_dict
from django.shortcuts import render, redirect as django_redirect
from django.urls import reverse
from django.http import HttpRequest

from .models import GoLink
from django.db.models import F
from django.views import generic


class IndexView(generic.ListView):
    template_name = "go/index.html"
    context_object_name = "golinks"
    paginate_by = 10
    model = GoLink
    ordering = "-hit_count"


def redirect(request: HttpRequest, short_url: str):
    # TODO: Treat empty original_url as a missing golink. Only unset the original_url when deleting golinks.
    # This way, we'll be able to retain hit_count for deleted golinks.
    try:
        golink = GoLink.objects.get(short_url=short_url)
        golink.hit_count = F("hit_count") + 1
        golink.save(update_fields=["hit_count"])
        return django_redirect(golink.original_url)
    except GoLink.DoesNotExist:
        return django_redirect(reverse("manage", args=[short_url]))


def manage(request: HttpRequest, short_url: str | None = None):
    if request.method == "POST":
        context = create_golink(request)
    else:
        context = model_to_dict(
            GoLink.objects.get_or_create(short_url=short_url)[0],
            fields=["short_url", "original_url", "hit_count"],
        )
    return render(
        request,
        "go/create.html",
        context=context,
    )


def create_golink(request: HttpRequest) -> dict[str, Any]:
    original_url = request.POST.get("original_url")
    short_url = request.POST.get("short_url")
    if not short_url:
        return {"error_message": "Please provide a short link name"}
    if not original_url:
        return {"error_message": "Please provide a URL to shorten"}
    golink, _ = GoLink.objects.get_or_create(short_url=short_url)
    golink.original_url = original_url
    golink.save()
    return model_to_dict(golink, fields=["short_url", "original_url", "hit_count"])

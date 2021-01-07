from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import GameForm


def createGame(request):
    if request.method == "GET":
        return render(
            request, "games/createGame.html",
            {"form": GameForm}
        )
    elif request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            return redirect(reverse("dashboard"))

def playGame(request):
    if request.method == "GET":
        return render(
            request, "games/playGame.html",
        )

def question1(request):
    if request.method == "GET":
        return render(
            request, "games/question1.html",
        )

def question2(request):
    if request.method == "GET":
        return render(
            request, "games/question2.html",
        )

def endScreen(request):
    if request.method == "GET":
        return render(
            request, "games/endScreen.html",
        )

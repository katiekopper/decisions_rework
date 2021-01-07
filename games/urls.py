from django.conf.urls import include, url
from games.views import createGame
from games.views import playGame
from games.views import question1
from games.views import question2
from games.views import endScreen

urlpatterns = [
    url(r"^createGame/", createGame, name="createGame"),
    url(r"^playGame/", playGame, name="playGame"),
    url(r"^question1/", question1, name="question1"),
    url(r"^question2/", question2, name="question2"),
    url(r"^endScreen/", endScreen, name="endScreen"),

]

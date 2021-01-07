from django import forms

# iterable
LENGTH_CHOICES = (
    ("1", "30 DAYS"),
    ("2", "60 DAYS"),
)

MONEY_CHOICES = (
    ("1", "$500"),
    ("2", "$1000")
)


class GameForm(forms.Form):
    title = forms.CharField(max_length=100, label='Name of Game')
    description = forms.CharField(max_length=100, label='Description of Game')
    length = forms.ChoiceField(choices=LENGTH_CHOICES, label='Choose the length of the game in days')
    money = forms.ChoiceField(choices=MONEY_CHOICES, label="Choose the amount of money a player begins with")
    decision = forms.CharField(max_length=200, label='Enter a Decision')
    option1 = forms.CharField(max_length=100, label='Enter the first choice')
    option2 = forms.CharField(max_length=100, label='Enter the second choice')



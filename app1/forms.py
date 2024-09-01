from django import forms

class booklocation(forms.Form):
    district=[('North Delhi','North Delhi'),('South Delhi','South Delhi'),('East Delhi','East Delhi'),('West Delhi','West Delhi'),('Central Delhi','Central Delhi')]
    type=[('Whole day','Whole Day'),('Monthly Basis','Monthly Basis'),('One time Travel','One Time Travel')]
    Name=forms.CharField()
    location=forms.ChoiceField(choices=district)
    type=forms.ChoiceField(choices=type)

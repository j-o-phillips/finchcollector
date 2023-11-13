from django.shortcuts import render

finches = [
    {'name': 'House finch', 'territory': 'North America'},
    {'name': "Cassin's finch", 'territory': 'U.S/Canada' }
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    return render(request, 'finches/index.html', { 'finches': finches})

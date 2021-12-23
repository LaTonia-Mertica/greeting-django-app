from django.shortcuts import render

# Create your views here.
def hello(request, name='code world'):
    if request.method == 'GET':
        return render(request=request, template_name='hello.html', context={'name': name})

def goodbye(request, name='code master haters'):
    if request.method == 'GET':
        return render(request=request, template_name='goodbye.html', context={'name': name})
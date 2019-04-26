from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request,'index.html') #fazer os itens aparecer

def sobre(request):
    return render(request,'sobre.html')
    
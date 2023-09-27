from .models import Aluno
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 # atenção na importação

#####################
def alunoView(request):
    alunos_list = Aluno.objects.all()
    return render(request, 'main/alunos.html', {'alunos_list':alunos_list})
####################

def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    print(aluno)
    return render(request, 'main/alunoID.html',{'aluno':aluno})
####################

def contact_view(resquest):
    if resquest.method =='POST':
        name = resquest.POST.get('name')
        email = resquest.POST.get('email')
        message = resquest.POST.get('message')
        print('name:', name)
        print('email:', email)
        print('message:', message)
    return render(resquest, 'main/contact.html')
        
        
        
        
    
from django.shortcuts import render


def list_item(request):
    students=['stud1','stud2','stud3','stud4']
    fruits=['apple','kiwi','pomogrante']
    
    context={
        "students":students,
        "fruits":fruits,
    }
    return render(request,'list_item.html',context)

# Create your views here.

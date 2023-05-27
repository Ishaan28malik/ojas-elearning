from django.shortcuts import render
from . models import Tutorial, Member
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def homepage(request):
    if request.method == "Post":
        student_name = request.Post['student_name']
        student_email = request.Post['student_email']
        student_country = request.Post['student_country']
        message_subject = request.Post['message_subject']
        message = request.Post['message']

        # send an email
        send_mail(
            message_subject,
            student_name + 'says' + message + student_country,
            student_email,
            [sahasrabudheoj@gmail.com],
            )
        return render(request, 'contact', context = {"student_name": student_name})
        
    else:
        return render(request = request,
                    template_name='main/newhome.html',
                    context = {"tutorials": Tutorial.objects.all, "members": Member.objects.all}, 
                    )


def language(request):
    return render(request = request,
                  template_name='main/index.html',
                  context = {"tutorials": Tutorial.objects.all, "members": Member.objects.all}, 
                  )


def culture(request):
    return render(request = request,
                  template_name='main/services.html',
                  context = {"tutorials": Tutorial.objects.all, "members": Member.objects.all}, 
                  )

def indianstudies(request):
    return render(request = request,
                  template_name='main/indian-studies.html',
                  context = {"tutorials": Tutorial.objects.all, "members": Member.objects.all}, 
                  )

def arjunmahabharata(request):
    return render(request = request,
                  template_name='main/arjun.html',
                  context = {"tutorials": Tutorial.objects.all, "members": Member.objects.all}, 
                  )

def spanish(request):
    return render(request = request,
                  template_name='main/spanish.html',
                  context = {"tutorials": Tutorial.objects.all, "members": Member.objects.all}, 
                  )

def stillasapling(request):
    return render(request = request,
                  template_name='main/sapling.html',
                  context = {"tutorials": Tutorial.objects.all, "members": Member.objects.all}, 
                  )


def contact(request):
    if request.method == "Post":
        student_name = request.Post['student_name']
        student_email = request.Post['student_email']
        student_country = request.Post['student_country']
        message_subject = request.Post['message_subject']
        message = request.Post['message']

        # send an email
        send_mail(
            message_subject,
            student_name + 'says' + message,
            student_email
            [sahasrabudheoj@gmail.com],
            )
        return render(request, 'contact', context = {"student_name": student_name})
    
    else:
        return render(request = request,
                    template_name='main/contact.html',
                    context = {"tutorials": Tutorial.objects.all, "members": Member.objects.all}, 
                    )
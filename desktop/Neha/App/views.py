from django.shortcuts import render
from .models import User
from django.template import loader
from django.http import HttpResponse
from .models import Transfer
#fromuser = 0
#touser = 0
def showuser(request,parameter):
    u1 = User.objects.get(id = parameter)
    t1 = Transfer.objects.filter(from_user_name = u1.Name)
    n1 = t1.count()
    t2 = Transfer(from_user_name = u1.Name)
    t2.save()
    t3 = Transfer.objects.filter(to_user_name = u1.Name)
    n2 = t3.count()
    if(n1>0):
        x = t1[n1-1]
        if(n2>0):
            y = t3[n2-1]
            context = {'u1':u1,'x':x,'y':y}
        else:
            y = 0
            context = {'u1':u1,'x':x,'y':y}
    elif(n2>0):
        x = 0
        y = t3[n2-1]
        context = {'u1':u1,'x':x,'y':y}
    if(n1 == 0 and n2 == 0):
        x = 0
        y = 0
        context = {'u1':u1,'x':x,'y':y}
    
    
    template = loader.get_template('html_ki_file/showuser.html')
     
    return HttpResponse(template.render(context,request))
    #return HttpResponse(" id:- "+str(u1.id)+"<br> "+"Name:- "+u1.Name+"<br>"+"E-mail:- "+u1.Email+"<br> "+"Credit:- "+u1.credit)
def hello(request):
    u1 = User.objects.all()
    template = loader.get_template('html_ki_file/hello.html')
    context = {'u1':u1} 
    return HttpResponse(template.render(context,request))
def alluser(request):
    u1 = User.objects.all()
    template = loader.get_template('html_ki_file/alluser.html')
    context = {'u1':u1} 
    return HttpResponse(template.render(context,request))
def creditsto(request):
    u1 = User.objects.all()
    template = loader.get_template('html_ki_file/creditsto.html')
    context = {'u1':u1} 
    return HttpResponse(template.render(context,request))
def transfer(request,parameter2):
    u1 = User.objects.get(id = parameter2)
    
    template = loader.get_template('html_ki_file/transfer.html')
    context = {'u1':u1} 
    #return HttpResponse("enter the credit number")
    return HttpResponse(template.render(context,request))
def last(request):
    t2 = Transfer.objects.last()
    u2 = User.objects.get(Name = t2.from_user_name)
    credit = u2.credit
    if(int(credit) < int(request.POST['text1'])):
        template1 = loader.get_template('html_ki_file/transfer.html')
        context = {'credit':credit}
        template2 = loader.get_template('html_ki_file/transfer2.html')
        return HttpResponse(template2.render(context,request)+template1.render(context,request))
    else:
        t1 = Transfer.objects.last()
        t1.transfer_credit = request.POST['text1']
        t1.save()
        t1 = Transfer.objects.last()
        u_from = User.objects.get(Name = t1.from_user_name)
        value1 = int(u_from.credit) - int(t1.transfer_credit)
        u_from.credit = str(value1)
        u_from.save()
        u_from = User.objects.get(Name = t1.from_user_name)
        u_to = User.objects.get(Name = t1.to_user_name)
        value2 = int(u_to.credit) + int(t1.transfer_credit)
        u_to.credit = str(value2)
        u_to.save()
        u_to = User.objects.get(Name = t1.to_user_name)
        template = loader.get_template('html_ki_file/last.html')
        context = {'t1':t1}
        return HttpResponse(template.render(context,request))
    
    #return HttpResponse("transfered succesfully"+t1.from_user_name+" "+t1.to_user_name+" "+t1.transfer_credit+" "+u_from.Name+" "+u_from.credit+" "+u_to.Name+" "+u_to.credit)
def TransferDetails(request):
    t1 = Transfer.objects.all()
    template = loader.get_template('html_ki_file/TransferDetails.html')
    context = {'t1':t1} 
    return HttpResponse(template.render(context,request))
def Cancel(request):
    t1 = Transfer.objects.last()
    t2 = Transfer.objects.all()
    n1 = t2.count()
    if(n1>0):
        t1.delete()
    u1 = User.objects.all()
    template = loader.get_template('html_ki_file/alluser.html')
    context = {'u1':u1} 
    return HttpResponse(template.render(context,request))
def showuser2(request,parameter3):
    u1 = User.objects.get(id = parameter3)
    p = parameter3
    t1 = Transfer.objects.filter(from_user_name = u1.Name)
    n1 = t1.count()
    t2 = Transfer.objects.last()
    t2.to_user_name = u1.Name
    t2.save()
    t3 = Transfer.objects.filter(to_user_name = u1.Name)
    n2 = t3.count()
    if(n1>0):
        x = t1[n1-1]
        if(n2>1):
            y = t3[n2-2]
            context = {'u1':u1,'x':x,'y':y,'p':p}
        else:
            y = 0
            context = {'u1':u1,'x':x,'y':y,'p':p}
    elif(n2>1):
        x = 0
        y = t3[n2-2]
        context = {'u1':u1,'x':x,'y':y,'p':p}
    if(n1 == 0 and n2 == 1):
        x = 0
        y = 0
        context = {'u1':u1,'x':x,'y':y,'p':p}
    template = loader.get_template('html_ki_file/showuser2.html')
     
    return HttpResponse(template.render(context,request))
    
    
                
    
    

# 
    
                
    
    

# Create your views here.

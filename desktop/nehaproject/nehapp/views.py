from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from nehapp.models import Movie
from django .template import loader
from nehapp.models import Songs
from nehapp.models import Details
def index(request):
    all_movies = Movie.objects.all()
    for a in all_movies:
        url = '/hello/' +str(a.id)+ '/'
        html = '<a href ="'+url+'">' + str(a.id) + '</a><br>'
    return HttpResponse("<h1> click on this to find actor name and movie_logo for actor of id:" +html+ "</h1>")
def showparms(request,parameter):
    #try:
        #movie = Movie.objects.get(id = int(parameter,base =10))
    #except Movie.DoesNotExist:
        #raise  Http404("movie_id doesnot exist heeeee")
    movie = get_object_or_404(Movie,id = parameter)
    return HttpResponse("<h1>the actor and actor_movie for this id is:" +movie.actor+"<br>"+ movie.movie_logo+"</h1>")
#Create your views here.
def temp(request):
    all_songs = Songs.objects.all()
    template = loader.get_template('html_ki_file/index.html')
    context = { 'all_songs':all_songs,} #a dictionary is use to pass data from view to template
    return HttpResponse(template.render(context,request))
def fav(request,par):
    movie = get_object_or_404(Movie,id = par)
    m1 = movie.songs_set.all()
    template = loader.get_template('html_ki_file/forms.html')
    context = { 'm1':m1,} #a dictionary is use to pass data from view to template
    return HttpResponse(template.render(context,request))
def favorite(request):
    #movie = get_object_or_404(Movie,id = parameter)
    selected_song = Songs.objects.get(id = request.POST['fav'])
    selected_song.save()
    return HttpResponse("<h1> your favorite song is:" + selected_song.song_name + "  its type is:" +selected_song.file_type +" and the actor is "+selected_song.movie.actor +"</h1>" )
def adding(request):
    m1 = Movie.objects.all()
    template = loader.get_template('html_ki_file/index1.html')
    context = {'m1':m1,}
    return HttpResponse(template.render(context,request))
def action(request) :
    a = Movie(actor = request.POST['text1'],actor_movie = request.POST['text2'],genre = request.POST['text3'],movie_logo = request.POST['text4'])
    a.save()
    return HttpResponse("<h1>"+ a.actor + "<br>" +a.actor_movie + "<br>" +a.genre+ "<br>"+ a.movie_logo+"<br>"+"a row is created" + "</h1>")
def show(request):
    m1 = Movie.objects.all()




    template = loader.get_template('html_ki_file/index2.html')
    context = {'m1':m1,}
    return HttpResponse(template.render(context,request))
def search(request):
    movies = Movie.objects.all()
    x = 0
    for a in movies:
        if str(a.id)== request.POST['text5']:
            x = a.id
    if x != 0:
        m0 = Movie.objects.filter(id = x)
        m1 = Movie.objects.filter(actor = request.POST['text5'])
        m2 = Movie.objects.filter(actor_movie = request.POST['text5'])
        m3 = Movie.objects.filter(genre = request.POST['text5'])
        m4 = Movie.objects.filter(movie_logo = request.POST['text5'])
        context = {'m0':m0,'m1':m1,'m2':m2,'m3':m3,'m4':m4,}
        template = loader.get_template('html_ki_file/index3.html')
        return HttpResponse(template.render(context,request))
    else:
        m1 = Movie.objects.filter(actor = request.POST['text5'])
        m2 = Movie.objects.filter(actor_movie = request.POST['text5'])
        m3 = Movie.objects.filter(genre = request.POST['text5'])
        m4 = Movie.objects.filter(movie_logo = request.POST['text5'])
        context = {'m1':m1,'m2':m2,'m3':m3,'m4':m4,}
        template = loader.get_template('html_ki_file/index4.html')
        return HttpResponse(template.render(context,request))
      
def signup(request):
    details = Details.objects.all()
    context = {'details':Details}
    template = loader.get_template('html_ki_file/signup.html')
    return HttpResponse(template.render(context,request))
def first_page(request):
    request.session['2'] = 'second'
    details = Details.objects.all()
    x = 0
    for a in details:
        if a.email_id == request.POST['text3']:
            x = x+1
    if x==0:
        a = Details(First_Name = request.POST['text1'],Last_Name = request.POST['text2'],email_id = request.POST['text3'],password = request.POST['text4'])
        a.save()
        context = {'details':details}
        template = loader.get_template('html_ki_file/eg.html')
        return HttpResponse("<h1> signup sucessfully "+a.First_Name+"</h1>"+template.render(context,request))
    if x!=0:
        context = {'details':details}
        template = loader.get_template('html_ki_file/login1.html')
        return HttpResponse("<h1>email_id already exist tryagain:-"+"<br>"+"</h1>" + template.render(context,request))

def login(request):
    details = Details.objects.all()
    if '2' in request.session:
        name = request.session['2']
        context = {'details':details}
        template = loader.get_template('html_ki_file/eg.html')
        return HttpResponse("<h1> hey! "+name+"<br>" +"</h1>"+template.render(context,request))
        
    else:
        context = {'details':details}
        template = loader.get_template('html_ki_file/login1.html')
        return HttpResponse(template.render(context,request))
def eg(request):
    
    details = Details.objects.all()
    x = 0
    for a in details:
        if a.email_id == request.POST['email'] and a.password == request.POST['password']:
            x = x+1
            context = {'details':details}
            request.session['2'] = a.First_Name
            template = loader.get_template('html_ki_file/eg.html')
            return HttpResponse("<h1> hey!" +a.First_Name+"<br>" +"</h1>"+template.render(context,request))
    if x==0:
        context = {'details':details}
        template = loader.get_template('html_ki_file/login1.html')
        return HttpResponse("<h1>email_id or password does'nt match tryagain" +"<br>" +"</h1>"+template.render(context,request))
def logout(request):
    details = Details.objects.all()
    try:
        del request.session['2']
    except KeyError:
        pass
    context = {'details':details}
    template = loader.get_template('html_ki_file/login1.html')
    return HttpResponse(template.render(context,request))
    

    
    
    
    
    


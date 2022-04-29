from itertools import count

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .filter import PersonFilter,PersonFilters
from django .core.paginator import  Paginator
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from.models import formregistration,userimage
from .models import userimage,reviews,Messages
from django.urls import reverse
# Create your views here.
def view(request):
    return render(request, "theme/home/index.html")
def logandregister(request):
    return render(request, "theme/login-and-register/index.html")

def register(request):
    if request.method == 'POST':

        firstname = request.POST['firstname'].capitalize()
        lastname = request.POST['lastname'].capitalize()
        username = request.POST['username']
        email = request.POST['email'].replace('' ,'').lower()
        password = request.POST['pass']
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect(logandregister)
        else:

            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = firstname
            myuser.last_name = lastname
            user = userimage(user=myuser)

            myuser.save()
            user.save()
            messages.success(request, "You Have Successfully Registered!!")
            return redirect(signin)

        return render(request, "theme/login-and-register/index.html")

def signin(request):
    if request.method == 'POST':
        username1 = request.POST['userlog']
        password1 = request.POST['passlog']
        user = authenticate(request, username=username1, password=password1)
        if user is not None:
            login(request, user)
            return redirect(loggedin)
        else:


            return redirect('login')

    else:

        return render(request, "theme/login-and-register/index.html")

def signout(request):
    logout(request)
    return redirect(signin)
def loggedin(request):

    return render(request,'theme/home/index.html')


def dashboard(request):
    ucount = User.objects.all().count()
    user_emp_count =formregistration.objects.all().count()
    professional = formregistration.objects.filter(field=1).count()
    local = formregistration.objects.filter(field=2).count()
    context = {'ucount':ucount,
               'empcount':user_emp_count,
               'professional':professional,
               'local':local,
               }
    filtered_persons = PersonFilters(
        request.GET,
        queryset=formregistration.objects.all()


    )

    context['filtered_persons'] = filtered_persons
    paginated_filtered_persons = Paginator(filtered_persons.qs, 2)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filtered_persons.get_page(page_number)
    context['person_page_obj'] = person_page_obj
    return render(request, 'dashboard/index.html', context=context)

def dashboardforms(request):
    return render(request,'dashboard/register.html')
@login_required()
def empregister(request):
    if request.user.is_authenticated:

        fname = request.POST['fname'].capitalize()
        lname = request.POST['lname'].capitalize()
        email = request.POST['email']
        mobile = request.POST['mobile']
        gender = request.POST['gender'].capitalize()
        image = request.FILES['Image']
        job = request.POST['job'].capitalize()
        jobtype = request.POST['type'].capitalize()
        field  = request.POST['field']
        wage = request.POST['wage']
        address = request.POST['address'].capitalize()
        about = request.POST['about'].capitalize()
        uname = request.POST['uname']
        if User.objects.filter(username=uname):
            fregister = formregistration(fname=fname,
                                        lname=lname,
                                        email=email,
                                        mobile=mobile,
                                        image=image,
                                        job=job,
                                        location=address,
                                        uname=uname,
                                        wage=wage,
                                        jobtype=jobtype,
                                        about=about,
                                        gender=gender,
                                        field =field)
            fregister.save()
            return redirect(dashboard)
            messages.success(request,"You Have Successfully Registered!!")


    return render(request,'dashboard/register.html')
    messages.error(request,"Invalid Username...!")
def empdisplay(request):
    disreg = formregistration.objects.all()
    return render(request,'dashboard/index.html',{'display':disreg})


def browsjobs(request):
    context = {}
    filtered_persons = PersonFilters(
        request.GET,
        queryset=formregistration.objects.all()
    )

    context['filtered_persons'] = filtered_persons
    paginated_filtered_persons = Paginator(filtered_persons.qs, 5)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filtered_persons.get_page(page_number)
    context['person_page_obj'] = person_page_obj
    return render(request, 'theme/brows-jobs/index.html', context=context)
"""
def services(request):

    return render(request,'theme/services/index.html')
    
    """
def pages(request):
    return render(request,'theme/pages/how-it-works/index.html')

def psellers(request):
    context = {}
    filtered_persons = PersonFilter(
        request.GET,
        queryset=formregistration.objects.all()
    )

    context['filtered_persons'] = filtered_persons

    paginated_filtered_persons = Paginator(filtered_persons.qs,4)
    page_number =request.GET.get('page')
    person_page_obj = paginated_filtered_persons.get_page(page_number)
    context ['person_page_obj'] = person_page_obj
    return render(request, 'theme/pages/sellers/index.html', context=context)

def professional(request):
    context = {}
    filtered_persons = PersonFilter(
        request.GET,
        queryset=formregistration.objects.filter(field=1)
    )

    context['filtered_persons'] = filtered_persons

    paginated_filtered_persons = Paginator(filtered_persons.qs, 4)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filtered_persons.get_page(page_number)
    context['person_page_obj'] = person_page_obj
    return render(request, 'theme/pages/sellers/index.html', context=context)



def local(request):
    context = {}
    filtered_persons = PersonFilter(
        request.GET,
        queryset=formregistration.objects.filter(field=2)
    )

    context['filtered_persons'] = filtered_persons

    paginated_filtered_persons = Paginator(filtered_persons.qs, 4)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filtered_persons.get_page(page_number)
    context['person_page_obj'] = person_page_obj
    return render(request, 'theme/pages/sellers/index.html', context=context)

def pfaq(request):
    return render(request,'theme/pages/faq/index.html')

def workers(request,pk):
    disreg = formregistration.objects.get(pk=pk)

    suggest = formregistration.objects.all()

    return render(request, 'theme/brows-jobs/workers/index.html', {'display': disreg,'suggest':suggest})
    #return render(request,'theme/brows-jobs/workers/index.html')


@login_required()
def review(request,pk):
    if request.method == 'POST':
        rating = request.POST['rating']
        subject = request.POST['subject'].capitalize()
        review = request.POST['review'].capitalize()
        usr = User.objects.get(id=request.user.id)
        userpost =usr.username
        uimg = userimage.objects.get(user__id=request.user.id)
        usrimage = uimg.image
        fname = usr.first_name
        lname = usr.last_name
        user = formregistration.objects.get(pk=pk)
        un = user.uname
        rev = reviews(rfname=fname,
                      rlname=lname,
                      rimg=usrimage,
                      rating=rating,
                      subject=subject,
                      review=review,
                      userget=un,
                      ruser=userpost)

        rev.save()



    disreg = formregistration.objects.get(pk=pk)
    userd = disreg.uname
    revdis = reviews.objects.filter(userget=userd)
    return render(request, 'theme/brows-jobs/workers/index.html',{'display': disreg,'revdisplay':revdis})


def org_update(request):
    if request.user.is_authenticated:
        usract = User.objects.get(id=request.user.id)
        usrname =usract.username
        account = formregistration.objects.get(uname=usrname)
        return render(request, 'dashboard/profile.html' ,{'account':account})

@login_required()
def profile_update_org(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            newfirstname = request.POST['newfirstname'].capitalize()
            newlastname = request.POST['newlastname'].capitalize()
            newusername = request.POST['newusername']
            newemail = request.POST['newemail'].replace('', '').lower()
            newpic =request.FILES.get('newpic')
            User.objects.filter(id=request.user.id).update(first_name=newfirstname,
                                                           last_name=newlastname,
                                                           username=newusername,
                                                           email=newemail)
            usr = userimage.objects.get(user__id = request.user.id)
            if 'newpic' not in request.FILES:
                usr.image = usr.image
            else:
                usr.image = newpic

            usr.save()
            #messages.success(request,'Your Profile Is Successfully Updated')
            return redirect(org_update)

"""
def filterr(request):
    price = request.POST['price-from']
    sjob = request.POST['project_seller_type']
    location = request.POST['locations']
    jobfltr = request.POST['work']
    disreg = formregistration.objects.filter(job=jobfltr,
                                             wage=price,
                                             jobtype=sjob,
                                             address=location)

    return render(request, 'theme/brows-jobs/filter1/index.html', {'fltrdisplay': disreg})



"""


def empupdate(request):


    return render(request, 'dashboard/login.html')
@login_required()
def emp_org_update(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            newfname = request.POST['newfirstname'].capitalize()
            newlname = request.POST['newlastname'].capitalize()
            newemail = request.POST['newemail']
            newmobile = request.POST['newmobile']
            newgender = request.POST['egender'].capitalize()
            newimage = request.FILES['newpic']
            newjob = request.POST['newjob'].capitalize()
            newjobtype = request.POST['newjobtype'].capitalize()
            newwage = request.POST['newwage']
            newaddress = request.POST['newaddress'].capitalize()
            newusername = request.POST['newusername']
            if User.objects.filter(username=newusername):
                formregistration.objects.filter(uname=newusername).update(fname=newfname,
                                                                          lname=newlname,
                                                                          email=newemail,
                                                                          mobile=newmobile,
                                                                          gender=newgender,
                                                                          image=newimage,
                                                                          job=newjob,
                                                                          jobtype=newjobtype,
                                                                          wage=newwage,
                                                                          location=newaddress,
                                                                          uname=newusername)
                return redirect(dashboard)


def about(request):
    ucount = User.objects.all().count()
    user_emp_count = formregistration.objects.all().count()
    professional = formregistration.objects.filter(field=1).count()
    local = formregistration.objects.filter(field=2).count()
    context = {'ucount': ucount,
               'empcount': user_emp_count,
               'professional': professional,
               'local': local,
               }
    filtered_persons = PersonFilters(
        request.GET,
        queryset=formregistration.objects.all()
    )

    context['filtered_persons'] = filtered_persons
    paginated_filtered_persons = Paginator(filtered_persons.qs, 4)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filtered_persons.get_page(page_number)
    context['person_page_obj'] = person_page_obj
    return render(request, 'theme/about/index.html',context=context)


def contact(request):
    return render(request, 'theme/contact/index.html')




@login_required()
def message(request, pk):
    if request.method == 'POST':
        message = request.POST['message'].capitalize()

        usr = User.objects.get(id=request.user.id)
        userpost = usr.username
        uimg = userimage.objects.get(user__id=request.user.id)
        usrimage = uimg.image
        fname = usr.first_name
        lname = usr.last_name
        user = formregistration.objects.get(pk=pk)
        un = user.uname
        msg = Messages(sender=message, mimg=usrimage, mfname=fname, mlname=lname, msgpost=userpost, msgget=un)
        msg.save()


    mg = formregistration.objects.get(pk=pk)
    musr = mg.uname
    msg = Messages.objects.filter(msgget=musr)

    return render(request, 'chat/index.html',{'msgdply': mg, 'msgg': msg})

def calendar(request):
    return render(request, 'dashboard/calendar.html')

"""
def show_all(request):
    context = {}
    filtered_persons = PersonFilter(
        request.GET,
        queryset=formregistration.objects.all()
    )

    context['filtered_persons'] = filtered_persons
    return render(request,'theme/success.html',context=context)
"""


@login_required()
def chat(request):

    return render(request, 'chat/app-chat.html')


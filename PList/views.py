from django.shortcuts import redirect, render
from PList.models import Barangay, Requirements , Admin , Certificate
from django.views.decorators.csrf import csrf_exempt

def home_page(request):
    return render(request, 'Userlog.html')
def user(request): 
 if request.method == 'POST':
        if Barangay.objects.filter(usr=request.POST['un'],pas=request.POST['ps']).exists():
            barangay_ = Barangay.objects.get(usr=request.POST['un'], pas=request.POST['ps'])
            return redirect(f'{barangay_.id}/view_list')

        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'Userlog.html', context)
def admin(request): 
 if request.method == 'POST':
        if Admin.objects.filter(usrname=request.POST['uname'],pasword=request.POST['psw']).exists():
            admin_ = Admin.objects.get(usrname=request.POST['uname'], pasword=request.POST['psw'])
            # return redirect(f'/certificate')
            return redirect(f'/certificate')
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'Adminlog.html', context)

def certificate(request):
    return render(request, 'certificate.html')


def certificateprint(request):
    pins= Certificate.objects.create(certificate = request.POST['cate'])
    return redirect('print')
    return render(request, 'certificate.html')

def print(request):
    prints = Certificate.objects.last()
    return render(request, 'print.html',{'prints': prints})

def zadmin(request):
    return render(request, 'Adminlog.html')


# def home_page(request):
#     barangays = Barangay.objects.all()
#     return render(request, 'Login.html',{'barangays': barangays})

def new_item(request):
    barangayt_= Barangay.objects.create(Tname = request.POST['lname'],birthday = request.POST['Fbirthday'],gender = request.POST['Genderselect'],address = request.POST['Faddress'],cnumber = request.POST['ccnumber'],email = request.POST['eaddress'],usr=request.POST['un'],pas=request.POST['ps'])
    return redirect('/')
    

def view_list(request,barangay_id):
    barangay_= Barangay.objects.get(id = barangay_id)
    #barangay = Tname.objects.filter(barangay = barangay_id)
    requirements= Requirements.objects.all()
    return render(request,'requirements.html', {'barangay': barangay_,'requirements': requirements})

def add_item(request,barangay_id):

    barangay_= Barangay.objects.get(id= barangay_id)
    Requirements.objects.create(swabresult=request.POST['Rswab'],RidtCard=request.POST['RidtCard'],identificationCards=request.POST['myfile'], Rtranspo=request.POST['Rtranspo'],transportation=request.POST['ptransportation'],Pname=request.POST['pname'],swabcertificate=request.POST['cef'],barangay=barangay_)
    return redirect(f'/{barangay_.id}/view_list')



def register(request):
    return render(request,'register.html')

def edit(request, id):
    barangays = Barangay.objects.get(id=id)
    context = {'barangays':barangays}
    return render(request, 'ssuppp.html', context)

def update(request, id):
    barangay = Barangay.objects.get(id=id)
    barangay.zbarangay =request.POST['NAME']
    barangay.municipal =request.POST['PHONE NUMBER']
    barangay.address=request.POST['Address']
    barangay.save()
    return redirect('/')

def delete(request, id):

    barangay = Barangay.objects.get(id=id)
    barangay.delete()
    return redirect('/')


def signup2(request):


    return render(request, 'Login.html')


def signup3(request):

    return render(request, 'ssup.html')

def signup4(request):

    return render(request, 'ssupp.html')











'''def home_page(request):
    barangays = Barangay.objects.all() 
    return render(request, 'home.html',{'barangays' : barangays })
def new

def login(request):
    #login_ = Barangay.objects.get(id=barangay_id)
    return render(request, 'Login.html')


def signup1(request):

    return render(request, 'Sgnup.html')

def signup2(request):


    return render(request, 'Signup.html')


def signup3(request):

    return render(request, 'ssup.html')

def signup4(request):

    return render(request, 'ssupp.html')'''







'''def new_list(request):
    barangay_ = Barangay.objects.create()
    #Item.objects.create(npet=request.POST['pet'],nname =request.POST['owner'],nAddress=request.POST['address'],nBreed =request.POST['breed'],nDay =request.POST['birthday'], barangay=barangay_)
    return redirect(f'/PList/{barangay_.id}/')

def add_item(request, barangay_id):
    barangay_ = Barangay.objects.get(id=barangay_id)
    #Item.objects.create(npet=request.POST['pet'],nBreed =request.POST['breed'],nDay =request.POST['birthday'],barangay=barangay_)
    return redirect(f'/PList/{barangay_.id}/')

def DataBarangay(request):
    userp = UserProfile(fullname="Justcasey", age="21", email="happykid@gmail.com", address="San antonio zambales")
    userp.save()

    userp = Barangay.objects.all()
    result = 'Printing all entries in UserProfile model : <br>'
    for x in userp:
        res += x.fullname+"<br>"

    userpp = Barangay.objects.get(id="1")
    res += 'Printing One Entry <br>'
    res += userpp.email

    res += '<br> Deleting an entry <br>'
    userpp.delete()

    userp = UserProfile(fullname="Justcasey", age="21", email="Justcasey@gmail.com", address="San antonio zambales")
    userp.save()
    res += 'Updating entry <br>'

    userp = UserProfile.objects.get(fullname="Justcasey")
    userp.Position = "Representative"
    userp.save()
    res = ""

    mf = UserProfile.objects.filter(fullname="Justcasey")
    res += "Found : %s results<br>"%len(qs)

    mf = UserProfile.objects.order_by(email="Justcasey@gmail.com")
    for x in qs:
        res += x.fullname + x.email +'<br>'''


'''def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(rmyname =request.POST['myname'],igs =request.POST['gs'],nGen =request.POST['Gen'],cadds=request.POST['adds'],enum =request.POST['num'],semaladd=request.POST['emaladd'],list=list_)
    return redirect(f'/PList/{list_.id}/')'''

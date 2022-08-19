from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#view is python function actually
from book.models import BookInfo
from django.http import HttpRequest
from django.http import HttpResponse
def index(request):

    #return HttpResponse('ok')
    """context = {
        'name':'11 is coming'
    }
    return render(request,'book/index.html', context=context)"""
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse('index')

#################add data#####################
from book.models import BookInfo
#way 1
book = BookInfo(
    name = 'Django',
    pub_date = '2001-1-1',
    readcount = 10
)
#we need to save by manually
book.save()

#way 2
#objects just like a proxy
#
BookInfo.objects.create(
    name = 'grandm2',
    pub_date = '1965-1-1',
    readcount = 10000
)


######################modify data##############################
#way 1
book=BookInfo.objects.get(id=6)#select * from bookinfo where id = 6

book.name = 'dog go'

#we need to use save functhon to save data
book.save()

#way 2
BookInfo.objects.filter(id=5).update(name='pythonbase',commentcount=666)
BookInfo.objects.filter(id=10).update(name='we',commentcount=10000)
######################delete data##############################

#way 1
book=BookInfo.objects.get(id=6)
#fisical delete and logical delete (is_delete = False)
book.delete()

#way 2
BookInfo.objects.get(id=6).delete()
BookInfo.objects.filter(id=6).delete()
BookInfo.objects.filter(id=7).delete()

######################query##############################
# get :query only one result
try:
    book = BookInfo.objects.get(id=6)
except BookInfo.DoesNotExist:
    print('no data')

# all :query multipule results
BookInfo.objects.all()
from book.models import PeopleInfo
PeopleInfo.objects.all()

# count: query result count
BookInfo.objects.all().count()
BookInfo.objects.count()

######################fiter query##############################
book = BookInfo.objects.get(id=1)
book = BookInfo.objects.get(id__exact=1)

BookInfo.objects.get(pk=1)

BookInfo.objects.get(id=1)
BookInfo.objects.filter(id=1)

BookInfo.objects.filter(name__contains='y')

BookInfo.objects.filter(name__endswith='e')

BookInfo.objects.filter(name__isnull=True)

BookInfo.objects.filter(id__in=[1,3,5])

BookInfo.objects.filter(id__gt=3)#gt:great lt:less gte: great equal lte:less equal

BookInfo.objects.exclude(id=3)

BookInfo.objects.filter(pub_date__year=1980)

BookInfo.objects.filter(pub_date__gt='1990-1-1')

###############################################################
from django.db.models import F

BookInfo.objects.filter(readcount__gte=F('commentcount'))

BookInfo.objects.filter(readcount__gte=F('commentcount')*2)
# readcount gt 20 and id lt 3
BookInfo.objects.filter(readcount__gt=20).filter(id=__lt=3)
# or
BookInfo.objects.filter(readcount__gt=20,id__lt=3)

# readount gt 20 or id lt 3
from django.db.models import Q
# model.objects.filter (Q()|Q()|...) or
# model.objects.filter (Q()&Q()|...) and
# model.objects.filter (~Q()) not
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))

#######################################################################
from  django.db.models import Sum,Max,Min,Avg,Count
#model.objects.aggregate(Xxx('feild'))

BookInfo.objects.aggregate(Sum('readcount'))

#######################order by###############################
BookInfo.objects.all().order_by('readcount')

#######################cascade###############################

book=BookInfo.objects.get(id=1)

book.peopleinfo_set.all()

person=PeopleInfo.objects.get(id=1)

person.book.name

#############################relation filter query#########################################
#
BookInfo.objects.filter(peopleinfo__name__exact='guojin')

BookInfo.objects.filter(people__description__contains='ba')

PeopleInfo.objects.filter(book__name='tianlongbabu')

PeopleInfo.objects.filter(book__readcount__gt=30)
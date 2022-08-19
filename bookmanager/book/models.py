from django.db import models

# Create your models here.

class BookInfo(models.Model):
    #id The system will give to us id
    #CharField must be setting length
    name=models.CharField(max_length=10,unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo' #modify table name
        verbose_name = 'book manage' #station use only
    #rewrite str function to show name'book by admin
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    #define an order dictional
    GENDER_CHOICE = (
        (1,'male'),
        (2,'female')
    )
    name = models.CharField(max_length=10,unique=True)#name can not have the same name
    gender = models.SmallIntegerField(choices=GENDER_CHOICE,default=1)
    description = models.CharField(max_length=100,null=True)
    is_delete = models.BooleanField(default=False)
    #foreign key
    #system will dipatch foreign key auto

    #foreign's cascade operate
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'
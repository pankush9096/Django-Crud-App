from django.db import models

# Create your models here.


class Login(models.Model):
    # table creation and models.Model is passed everytime to inherit from pre made classes in django admin page.

    username = models.CharField(max_length=30, unique=True)
    # attribute or column name of table, Primary Key 'ID' will already be generated.

    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    DOB =  models.DateField()


    Gender = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('NA', 'Not Applicable')
    )

    gender = models.CharField(max_length=10, choices=Gender, default= 'NA')

    def __str__(self):
        # as record added in login will show as object number so this function will return it as name.
        return self.username


class Python(models.Model):
    session = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.session

class students(models.Model):
    Name = models.CharField(max_length=30, unique= True, primary_key= True)
    session = models.ForeignKey("Python",on_delete= models.PROTECT)
    # making session column from Python table as foreign key in table students.
    # on_delete will help if we delete table Python it will protect already filled data of students.
    # on making primary key as True, django will remove default primary key 'ID'.

    def __str__(self):
        return self.Name


#Introduction to ModelForm using this model in forms

class Register(models.Model):
    name= models.CharField(max_length=30)
    email = models.EmailField(max_length=30 )
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.name



from django.db import models

# Create your models here.
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=255)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),
                                                  ('Non IT','Non IT'),
                                                  ('Mobile Phones','Mobile Phones')
                                                  ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name


#Create your Employee model
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=255)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=255,choices=(
        ('Manager','Manager'),
        ('Software Engineer','Software Engineer'),
        ('Project Lead','Project Lead')
    ))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

#Create your project model

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    start_date=models.DateTimeField(auto_now=True)
    end_date=models.DateTimeField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    employee=models.ManyToManyField(Employee)
    status=models.CharField(max_length=100,choices=(
        ('In Progress','In Progress'),
        ('Completed','Completed'),
        ('On Hold','On Hold')
    ))

    def __str__(self):
        return self.title
    


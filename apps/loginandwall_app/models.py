from __future__ import unicode_literals

from django.db import models

import re

# Create your models here.

class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {'status': True, 'errors':[]}
        if not postData['first_name'] or len(postData['first_name']) < 2:
            results['status']=False
            results['errors'].append("First name must be more than one character.")
        if not postData['last_name'] or len(postData['last_name']) < 2:
            results['status']=False
            results['errors'].append("Last name must be more than one character.")
        if not postData['email'] or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", postData['email']):
            results['status']=False
            results['errors'].append("Email address is not valid.")
        if not postData['password'] or len(postData['password'])< 8 or postData['password']!=postData['confirmpw']:
            results['status']=False
            results['errors'].append("Please make sure passwords match and are at least 8 character.")
        if results['status']==True:
            user = User.objects.filter(email=postData['email'])
            if len(user)!=0:
                results['status']=False
                results['errors'].append("User already exists. Please use a different email address.")
            else:
                User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=postData['password'])
                return results
        return results

    def loginVal(self, postData):
        results = {'status':True, 'errors':[], 'user':{}, 'name':""}
        if not postData['email'] or not postData['password']:
            results['status']=False
            results['errors'].append("Login failed. Please try again.")
            return results
        else:
            user = User.objects.filter(email=postData['email'])
            if user[0].password != postData['password']:
                results['status']=False
                results['errors'].append("Login failed. Please try again.")
            else:
                results['errors'].append("Login Successful!")
                results['user']=user
                results['name']=user[0].first_name
            return results


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    objects = UserManager()


from msilib.schema import Class
from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models

class Igreja(models.Model):
    nome = models.CharField(max_length=150, unique=True, verbose_name='nome')
    religiao = models.CharField(max_length=150, verbose_name='religião')
    local = models.CharField(max_length=150, verbose_name='Local')
    id = models.AutoField(auto_created=True, primary_key=True, unique=True)

    
    
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ("id",)

class Culto(models.Model):
    nome_do_culto = models.CharField(max_length=150)
    descricao = models.TextField(max_length=150,verbose_name='descrição')
    data = models.DateTimeField('data/hora',null=True,blank=True)

    igreja = models.ForeignKey(Igreja, on_delete=models.CASCADE, default=True)
    

 
    

    def __str__(self):
        return "{}-({})_______{}".format(self.nome_do_culto, self.igreja.nome, self.data)

    class Meta:
        ordering = ["data"] 


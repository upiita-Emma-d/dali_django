from distutils.command.upload import upload
from pyexpat import model
from tabnanny import verbose
from turtle import title
from django import forms
from django.db import models


# Create your models here.

class ImagenBase(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to ='images')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'imagen'
        verbose_name_plural = 'imagenes'


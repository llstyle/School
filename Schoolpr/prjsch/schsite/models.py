from django.db import models
from datetime import date
from django.urls import reverse
from django.conf import settings

# Create your models here.

class Klass(models.Model):
    klass = models.CharField("Класс", max_length=100, default=5)
    def __str__(self):
        return self.klass
    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"
class Items(models.Model):
    title = models.CharField("Название предмета", max_length=100)
    predmet = models.ManyToManyField(Klass, verbose_name="Предметы", blank=True)
    url = models.CharField("Название предмета на Англ", max_length=100, default='I dont know')
    def __str__(self) :
        return self.title
    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
class Teachers(models.Model):
    image = models.ImageField("Изоброжение",upload_to='media', blank=True) 
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    it = models.ManyToManyField(Items, verbose_name='Предмет' , null=True)
    def __str__(self) :
        return self.author.username
    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
class Students(models.Model):
    image = models.ImageField("Изоброжение",upload_to='media', blank=True) 
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    klas = models.ForeignKey(Klass, verbose_name="Класс", on_delete=models.SET_NULL, null=True)
    item = models.ManyToManyField(Items, verbose_name="Предметы", blank=True)
    def __str__(self):
        return self.author.username
    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"



class kolUrok(models.Model):
    title = models.CharField("Название Урока", max_length=100)
    data = models.DateField("Время задания", default=date.today)
    sdacha = models.DateField("Время сдачи", default=date.today)
    homework = models.CharField("Домашнее задание", max_length=100, blank=True)
    imgwork = models.ImageField("Изоброжение дз",upload_to='media', blank=True)
    genres = models.ManyToManyField(Students, verbose_name="Пресудствующие ученики", blank=True)
    item = models.ForeignKey(Items, verbose_name="Предмет", on_delete=models.CASCADE)
    nomer = models.PositiveIntegerField("Номер Урока", default="", blank=True)
    def __str__(self) :
        return self.item.title + " Урок № " + str(self.nomer)
    class Meta:
        abstract = False
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
class Password1(models.Model):
    password = models.CharField("Пороль, минимум 8 символов", max_length=20)
    def __str__(self) :
        return self.password
    class Meta:
        verbose_name = "пороль"
        verbose_name_plural = "пороли"


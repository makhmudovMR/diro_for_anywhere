from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
# from django.utils.timezone import now


def upload_files(instance, filename):
    return "files/{0}/{1}".format(instance.name, filename)

def upload_slides(instance, filename):
    return "slides/{0}/{1}".format(instance.name, filename)


def upload_bannerlinks(instance, filename):
    return "bannerlinks/{0}/{1}".format(instance.name, filename)


class News(models.Model):

    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    text = RichTextUploadingField(blank=True, null=True, verbose_name='Вопрос')
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Files(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя файла')
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name='Описание файла')
    file = models.FileField(upload_to=upload_files, verbose_name='Файл')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Архив'
        verbose_name_plural = 'Архив'


class Banner(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя слайда')
    slide = models.ImageField(upload_to=upload_slides)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'


class BannerLinks(models.Model):

    name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Имя ссылки")
    image = models.ImageField(upload_to=upload_bannerlinks, verbose_name='Изображение')
    link = models.CharField(max_length=999, blank=True, null=True, verbose_name='Вставьте ссылку')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
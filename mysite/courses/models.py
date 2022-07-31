from django.db import models
from django.urls import reverse


class Course(models.Model):
    slug = models.SlugField('Уникальное название курса')
    title = models.CharField('Название курса', max_length=120)
    desc = models.TextField('Описаниe')
    img = models.ImageField('Изображение', default='default.png', upload_to='course_images')
    is_free = models.BooleanField('Free?', default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug': self.slug})

class Lesson(models.Model):
    slug = models.SlugField('Уникальное название курса')
    title = models.CharField('Название курса', max_length=120)
    desc = models.TextField('Описаниe')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Which course?')
    number = models.IntegerField('Number of course')
    video = models.CharField('Video URL', max_length=100)

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})

    def __str__(self):
        return self.title
    
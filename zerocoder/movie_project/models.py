from django.db import models

class Reviews_post(models.Model):
  title = models.CharField('Название фильма', max_length=50)
  description = models.CharField('Описание фильма', max_length=200)
  movie_review = models.TextField('Отзыв о фильме')
  author = models.CharField('ФИО', max_length=200, default='Неизвестный автор')

  def __str__(self):
    return self.title
  
  
  
  
  class Meta:
    verbose_name = 'Кинопроект'
    verbose_name_plural = 'Кинопроекты'
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    birth_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title

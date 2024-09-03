from celery import shared_task
from .models import Task, Comment
import datetime


@shared_task
def check_prohibited_words(comment_id):
    comment = Comment.objects.get(id=comment_id)
    prohibited_words = ['продать', 'крипта', 'ставки']
    for word in prohibited_words:
        comment.text = comment.text.replace(word, '###')
    comment.save()


@shared_task
def check_deadlines():
    tasks = Task.objects.filter(due_date__lte=datetime.date.today())
    for task in tasks:
        task.due_date += datetime.timedelta(days=1)
        task.save()

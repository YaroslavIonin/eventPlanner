from config.celery import app

from apps.events.models import Event


@app.task()
def push_notification(pk):
    event = Event.objects.get(pk=pk)
    event.event_description = 'Я изменился'
    event.save()
    print(event.id)
    print(event.main_name)
    print(event.event_date)
    print(event.event_time_start)
    print(event.event_time_finish)

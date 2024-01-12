from datetime import datetime, timedelta

from apps.events.models import Event

from apps.events.tasks import push_notification


def add_to_query_celery(pk):
    event = Event.objects.get(pk=pk)
    year = event.event_date.year
    month = event.event_date.month
    day = event.event_date.day
    hour = event.event_time_start.hour
    minute = event.event_time_start.minute
    date = datetime(
        year=year,
        month=month,
        day=day,
        hour=hour,
        minute=minute,
    )
    if date > datetime.now():
        eta_time = date - timedelta(minutes=3, hours=5)
        push_notification.s(pk=event.id).apply_async(eta=eta_time)

from datetime import datetime, timedelta
from ..models import Event, Schedule, DaySchedule


def create_schedule(name, date_start, date_finish, days):
    schedule = Schedule.objects.create(
        name=name,
        date_start=date_start,
        date_finish=date_finish,
    )
    days_schedule = []
    for day in days:
        days_schedule.append(
            DaySchedule(
                day_of_week=day['day_of_week'],
                time_start=day['time_start'],
                time_finish=day['time_finish'],
                schedule=schedule,
            )

        )
    DaySchedule.objects.bulk_create(days_schedule)
    return schedule.id


def create_with_schedule(data, user):
    schedule_id = create_schedule(
        name=data['main_name'],
        date_start=data['schedule']['date_start'],
        date_finish=data['schedule']['date_finish'],
        days=data['schedule']['days']
    )
    schedule = Schedule.objects.get(pk=schedule_id)

    days = schedule.days.all()
    days_of_week = days.values_list('day_of_week', flat=True)

    date_start = schedule.date_start
    date_finish = schedule.date_finish
    datedelta = timedelta(days=1)

    new_events = []
    while date_start <= date_finish:

        weekday = date_start.weekday() + 1
        if weekday in days_of_week:

            day = days.get(
                day_of_week=weekday
            )
            new_events.append(
                Event(
                    owner_id=user,
                    main_name=data['main_name'],
                    event_date=date_start,
                    event_time_start=day.time_start,
                    event_time_finish=day.time_finish,
                    location_id=data['location'],
                    event_description=data['event_description'],
                    child_id=data['child'],
                    schedule_id=schedule_id
                )
            )
        date_start += datedelta
    Event.objects.bulk_create(new_events)
    return {
        'message': 'success'
    }


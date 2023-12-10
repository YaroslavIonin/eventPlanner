from datetime import datetime
from ..models import Event, Schedule, DaySchedule


def create_schedule(name, days):
    schedule = Schedule.objects.create(name=name)
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


def create_with_schedule(data):
    schedule_id = create_schedule(
        name=data['main_name'],
        days=data['schedule']['days']
    )
    schedule = Schedule.objects.get(pk=schedule_id)
    days = schedule.days.all()
    breakpoint()


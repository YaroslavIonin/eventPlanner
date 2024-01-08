from django.db.models import QuerySet
from django_filters import rest_framework as filters, DateFilter

from ..models import Event


class EventFilterSet(filters.FilterSet):
    date = DateFilter(
        field_name='event_date',
        lookup_expr='gte',
    )
    month = DateFilter(
        field_name='event_date',
        method='custom_filter_date_by_month',
    )
    week = DateFilter(
        field_name='event_date',
        method='custom_filter_date_by_week',
    )

    class Meta:
        model = Event
        fields = ['date', 'month', 'child']

    def custom_filter_date_by_month(self, queryset: QuerySet, name, value):
        queryset = queryset.filter(
            event_date__month=value.month,
            event_date__year=value.year,
        )
        return queryset

    def custom_filter_date_by_week(self, queryset: QuerySet, name, value):
        year, week, _ = value.isocalendar()
        queryset = queryset.filter(
            event_date__week=week,
            event_date__year=year,
        )
        return queryset

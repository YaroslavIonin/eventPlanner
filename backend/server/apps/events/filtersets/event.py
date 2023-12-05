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
        method='custom_filter_date',
    )

    class Meta:
        model = Event
        fields = ['date', 'month']

    def custom_filter_date(self, queryset: QuerySet, name, value):
        queryset = queryset.filter(
            event_date__month=value.month,
            event_date__year=value.year,
        )
        return queryset

import django_filters
from django_filters import FilterSet
from .models import Post, Author
from django import forms

class PostFilter(FilterSet):
    name = django_filters.CharFilter(field_name='title',
                                            label="Поиск по названию",
                                            lookup_expr='icontains',)
    author = django_filters.ModelChoiceFilter(field_name='author',
                                              label='Выбор автора',
                                              lookup_expr='exact',
                                              queryset=Author.objects.all())
    date = django_filters.DateFilter(field_name='created_at',
                                        widget=forms.DateInput(attrs={'type': 'date'}),
                                        label='Дата',
                                        lookup_expr='date__gte')
    text = django_filters.CharFilter(field_name='text',
                                     label="Поиск по словам",
                                     lookup_expr='contains', )


    class Meta:
        model = Post
        fields = []
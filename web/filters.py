from django_filters import rest_framework as filters
from django_filters.widgets import RangeWidget
from .models import Post

class PostFilter(filters.FilterSet):
    min_like_count = filters.NumberFilter(field_name='like_count', lookup_expr='gte', label='Min Like Count')
    max_like_count = filters.NumberFilter(field_name='like_count', lookup_expr='lte', label='Max Like Count')
    created_at = filters.DateFromToRangeFilter(field_name='created_at', widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = ['created_at', 'author', 'min_like_count', 'max_like_count']

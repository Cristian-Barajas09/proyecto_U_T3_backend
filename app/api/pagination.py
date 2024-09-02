"""Custom pagination class."""
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    """Custom pagination class."""
    page_size = 10  # Número de elementos por página
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'current_page': self.page.number,
            'next_page': self.page.next_page_number() if self.page.has_next() else None,
            'last_page': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
            'results': data
        })
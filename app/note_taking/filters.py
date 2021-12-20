from rest_framework import filters


class CustomSearchFilter(filters.SearchFilter):
    """
    Customer search filter to return the search field as tags
    if tags is present in the query parameter as true else call super.
    """
    def get_search_fields(self, view, request):
        if request.query_params.get('tags'):
            return ['tags']
        return super().get_search_fields(view, request)

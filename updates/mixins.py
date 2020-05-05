from django.http import JsonResponse


class JSONResonseMixin(object):
    def render_to_json_response(self, context, **kwargs):
        return JsonResponse(data=context, **kwargs)

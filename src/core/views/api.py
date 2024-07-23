from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie
import json

from core.services.property.serialize_property import serialize_property
from core.services.property.search_properties import search_properties
from core.services.property.group_properties_by_assessment import (
    group_properties_by_assessment,
    )


@require_http_methods(["GET"])
def search_properties_view(request):
    lot = request.GET.get('lot')
    section = request.GET.get('section')
    deposited_plan = request.GET.get('deposited_plan')
    street_address = request.GET.get('street_address')

    properties = search_properties(
        lot,
        section,
        deposited_plan,
        street_address
        )
    grouped_properties = group_properties_by_assessment(properties)

    serialized_grouped_properties = {
        assessment: [serialize_property(prop) for prop in props]
        for assessment, props in grouped_properties.items()
    }

    return JsonResponse(serialized_grouped_properties)


@require_http_methods(["POST"])
@ensure_csrf_cookie
def select_assessment_view(request):
    data = json.loads(request.body)
    selected_assessment = data.get('selected_assessment')
    grouped_properties = data.get('grouped_properties', {})

    selected_properties = grouped_properties.get(selected_assessment, [])

    return JsonResponse({
        'selected_properties': selected_properties,
        'selected_assessment': selected_assessment
    })

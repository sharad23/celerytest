from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


@api_view(["GET"])
@permission_classes((AllowAny,))
def test5(request):
    from apple.tasks import add_numbers
    try:
        add_numbers.delay(1, 3)
        return Response({'result': 'success'})

    except Exception as e:
        print('here')
        return Response({'result': 'failure'})

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import asyncio

from .models import DreamInterpretation
from .serializers import DreamInterpretationSerializer
from .services import DreamInterpreter


@api_view(["POST"])
def interpret_dream(request):
    serializer = DreamInterpretationSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    dream_record = serializer.save()

    try:
        interpreter = DreamInterpreter()
        interpretation = asyncio.run(
            interpreter.interpret_dream(dream_record.dream_description)
        )

        dream_record.interpretation = interpretation
        dream_record.save()

        return Response(
            DreamInterpretationSerializer(dream_record).data, status=status.HTTP_200_OK
        )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

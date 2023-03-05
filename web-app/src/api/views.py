import asyncio

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.parsers import FileUploadParser

from .serializers import VendorCodeSerializer
from .service import get_api_info_codes, parse_xlsx
      

class VendorCodeAPIView(APIView):
    serializer_class = VendorCodeSerializer
    
    def post(self, request, file=None, format=None):
        serializer = VendorCodeSerializer(data=request.data)
        parser_classes = (FileUploadParser,)
        serializer.is_valid(raise_exception=True)
        
        if 'vendor_code' in serializer.data:
            codes = [serializer.data['vendor_code']]
        else:
            codes = parse_xlsx(request.data['vendor_code_file'])

        data = asyncio.run(get_api_info_codes(codes))
        return Response(data, status=HTTP_200_OK)

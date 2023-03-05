from rest_framework import serializers


class VendorCodeSerializer(serializers.Serializer):
    vendor_code = serializers.CharField(required=False)
    vendor_code_file = serializers.FileField(required=False)

    def validate(self, data):
        keys_set = {'vendor_code', 'vendor_code_file'}
        if len(set(data.keys()) & keys_set) != 1:
            raise serializers.ValidationError('Choice one field!')
        return data

    class Meta:
        fields=('vendor_code', 'vendor_code_file')

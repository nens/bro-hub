from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from api.mixins import RequiredFieldsMixin, UrlFieldMixin
from gmn import models as gmn_models

from . import models as gmw_models


class GMWSerializer(UrlFieldMixin, RequiredFieldsMixin, serializers.ModelSerializer):
    linked_gmns = serializers.SerializerMethodField()

    class Meta:
        model = gmw_models.GMW
        fields = "__all__"

    def get_linked_gmns(self, obj):
        try:
            linked_gmns = set(
                measuringpoint.gmn.uuid
                for measuringpoint in gmn_models.Measuringpoint.objects.filter(
                    gmw_bro_id=obj.bro_id
                )
            )
            return list(linked_gmns)

        except ObjectDoesNotExist:
            return None


class MonitoringTubeSerializer(
    UrlFieldMixin, RequiredFieldsMixin, serializers.ModelSerializer
):
    gmw_well_code = serializers.SerializerMethodField()

    class Meta:
        model = gmw_models.MonitoringTube
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True

    def get_gmw_well_code(self, obj):
        try:
            return gmw_models.GMW.objects.get(uuid=obj.gmw.uuid).well_code
        except ObjectDoesNotExist:
            return None

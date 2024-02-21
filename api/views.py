from rest_framework import status, generics, views
from rest_framework.response import Response
from django.urls import reverse
from rest_framework.reverse import reverse as drf_reverse


from . import tasks
from . import serializers
from . import models
from . import mixins


class APIOverview(views.APIView):
    def get(self, request, format=None):
        data = {
            "importtasks": drf_reverse(
                "api:importtask-list", request=request, format=format
            ),
            "uploadtasks": drf_reverse(
                "api:uploadtask-list", request=request, format=format
            ),
            "gmns": drf_reverse("api:gmn:gmn-list", request=request, format=format),
            "measuringpoints": drf_reverse(
                "api:gmn:measuringpoint-list", request=request, format=format
            ),
            "gmws": drf_reverse("api:gmw:gmw-list", request=request, format=format),
            "monitoringtubes": drf_reverse(
                "api:gmw:monitoringtube-list", request=request, format=format
            ),
        }
        return Response(data)


class ImportTaskListView(mixins.UserOrganizationMixin, generics.ListAPIView):
    """
    This endpoint handles the import of data from the BRO.
    As input, it takes one of the four possible BRO Objects (GMN, GMW, GLD, FRD).
    It saves the imported data in the corresponding datamodel.
    The progress can be followed in the generated import task instance.

    **POST Parameters**

    `BRO object`:
        String (*required*) options: 'GMN', 'GMW', 'GLD', 'FRD'
    """

    serializer_class = serializers.ImportTaskSerializer
    queryset = models.ImportTask.objects.all()
    
    def get(self, request, *args, **kwargs):
        """List of all Import Tasks."""
        return self.list(request, *args, **kwargs)

    def post(self, request):
        """
        Initialize an import task by posting a BRO object.
        """

        serializer = serializers.ImportTaskSerializer(data=request.data)

        if serializer.is_valid():
            import_task_instance = serializer.save()

            # Collect the relevant data
            import_task_instance_uuid = import_task_instance.uuid
            user_profile = models.UserProfile.objects.get(user=request.user)
            data_owner = user_profile.organisation

            # Update the instance of the new task
            import_task_instance.status = "PENDING"
            import_task_instance.data_owner = data_owner
            if not import_task_instance.kvk_number:
                import_task_instance.kvk_number = data_owner.kvk_number
            import_task_instance.save()

            # Start the celery task
            tasks.import_bro_data_task.delay(import_task_instance_uuid)

            # Get the dynamic URL using reverse
            url = reverse(
                "api:importtask-detail", kwargs={"uuid": import_task_instance.uuid}
            )
            full_url = request.build_absolute_uri(url)

            return Response(
                {
                    "message": f"Succesfully received the import taks request. Check {full_url} for the status of the import task."
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImportTaskDetailView(mixins.UserOrganizationMixin, generics.RetrieveAPIView):
    queryset = models.ImportTask.objects.all()
    serializer_class = serializers.ImportTaskSerializer
    lookup_field = "uuid"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UploadTaskListView(mixins.UserOrganizationMixin, generics.ListAPIView):
    """This endpoint handles the upload of data to the BRO.

    It takes the registration type, request type and the sourcedocument data as input.
    This API handles the transformation, validation and delivery of the data.
    The status of this proces can be followed in the generated upload task instance.
    """

    serializer_class = serializers.UploadTaskSerializer
    queryset = models.UploadTask.objects.all()

    def get(self, request, *args, **kwargs):
        """List of all Upload Tasks."""
        return self.list(request, *args, **kwargs)

    def post(self, request):
        """
        Initialize an upload task by posting the bro_domain, registartion_type, request_type, and the sourcedocument_data
        """

        serializer = serializers.UploadTaskSerializer(data=request.data)

        if serializer.is_valid():
            upload_task_instance = serializer.save()

            # Update the instance of the new task
            upload_task_instance.status = "PENDING"
            upload_task_instance.save()

            # Accessing the authenticated user's username and token
            user_profile = models.UserProfile.objects.get(user=request.user)
            username = user_profile.bro_user_token
            password = user_profile.bro_user_password
            project_number = user_profile.project_number

            # Start the celery task
            tasks.upload_bro_data_task.delay(
                upload_task_instance.uuid, username, password, project_number
            )

            # Get the dynamic URL using reverse
            url = reverse(
                "api:uploadtask-detail", kwargs={"uuid": upload_task_instance.uuid}
            )
            full_url = request.build_absolute_uri(url)

            return Response(
                {
                    "message": f"Succesfully received the upload taks request. Check {full_url} for the status of the import task."
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UploadTaskDetailView(mixins.UserOrganizationMixin, generics.RetrieveAPIView):
    queryset = models.UploadTask.objects.all()
    serializer_class = serializers.UploadTaskSerializer
    lookup_field = "uuid"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

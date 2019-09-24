from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status as status_codes

from django.http import Http404
from django.shortcuts import get_object_or_404

from main.models import Task, Block, MainUser
from main.serializers import TaskSerializerCreateUpdate, TaskSerializerGet


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskSerializerGet
        else:
            return TaskSerializerCreateUpdate

    def perform_create(self, serializer):
        creator = self.request.user
        executor = get_object_or_404(MainUser, pk=self.request.data['executor_id'])
        block = get_object_or_404(Block, pk=self.request.data['block_id'])
        if serializer.is_valid():
            serializer.save(creator=creator, executor=executor, block=block)
            return Response(serializer.data)
        return Response(serializer.errors, status=status_codes.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        executor = get_object_or_404(MainUser, pk=self.request.data['executor_id'])
        block = get_object_or_404(Block, pk=self.request.data['block_id'])
        if serializer.is_valid():
            serializer.save(executor=executor, block=block)
            return Response(serializer.data)
        return Response(serializer.errors, status=status_codes.HTTP_400_BAD_REQUEST)
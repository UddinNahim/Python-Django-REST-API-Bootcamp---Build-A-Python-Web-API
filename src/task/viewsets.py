from rest_framework import viewsets, mixins

from .serializers import TaskListSerializer ,TaskSerializer ,AttachementSerializer

from .models import Task,TaskList,Attachment


from .permissions import IsAllowedToEditTaskListElseNone,IsAllowedToEditTaskElseNone,IsAllowedToEditingAttachmentElseNone

class TaskListViewSet(mixins.CreateModelMixin,
                      
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
        
        permission_classes= [IsAllowedToEditTaskListElseNone,]
        
        queryset = TaskList.objects.all()
        serializer_class = TaskListSerializer

class TaskViewSet(viewsets.ModelViewSet):
        permission_classes = [IsAllowedToEditTaskElseNone,]
        queryset = Task.objects.all()
        serializer_class = TaskSerializer

        def get_queryset(self):
                queryset = super(TaskViewSet,self).get_queryset()
                user_profile = self.request.user.profile
                updated_queryset = queryset.filter(created_by = user_profile)
                return updated_queryset

class AttachmentViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,
                        viewsets.GenericViewSet):
        permission_classes = [IsAllowedToEditingAttachmentElseNone]
        queryset = Attachment.objects.all()
        serializer_class = AttachementSerializer


    

    
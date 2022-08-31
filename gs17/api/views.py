from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here

#1)BasicAuthentication
#Here we are using //IsAuthenticated// permission i.e no 2!!
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    permission_classes=[IsAdminUser]
    # permission_classes=[IsAuthenticatedOrReadOnly]

#Types of permissions Classes--

#1)AllowAny (Always available BYDEFAULT)
#2)IsAuthenticated
#3)IsAdminUser
#4)IsAuthenticatedOrReadOnly
#5)DjangoModelPermissions
#6)DjangoModelPermissionsOrAnonReadOnly
#7)DjangoObjectPermissions
#8)CustomPermissions


#Types of Authentication--

#1)BasicAuthentication
#2)SessionAuthentication
#3)TokenAuthentication
#4)RemoteUserAuthentication
#5)CustomAuthentication
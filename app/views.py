from django.http import HttpResponse
from django.shortcuts import render
from app.models import UserModel1,ActivityModel1
import io
from rest_framework.parsers import JSONParser
from app.serializers import UserSerializer,ActivitySerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.





def restAPI(request):

    act=ActivityModel1.objects.all()
    # user = UserModel1.objects.filter(activitymodel1=act.filter('id'))
    user=UserModel1.objects.all()
    print(user)
    ud = UserSerializer(user, many=True)
    json_data=JSONRenderer().render(ud.data)
    # print(json_data)

    # a=ActivitySerializer(act,many=True)

    # json_data1= JSONRenderer().render(a.data)
    # print(json_data1)
    return HttpResponse(json_data,content_type="application/json")
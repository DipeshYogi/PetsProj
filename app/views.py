from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
#from django.contrib.auth.mixins import LoginRequiredMixin
from app import conn_db
from rest_framework.permissions import IsAuthenticated


class BlogViews(APIView):
    permission_clsses = (IsAuthenticated,)

    def get(self,request):
        db = conn_db.get_conn()
        result = db.execute("select * from pets_care.blog")
        return Response(result)

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializer import LivrosSerializer
from apps.livros.models import Livros

class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livros.object.all()
    serializer_class = LivrosSerializer

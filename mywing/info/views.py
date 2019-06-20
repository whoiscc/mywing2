#

from rest_framework import generics
from mywing.info.models import News, Board
from mywing.info.serializers import NewsSerializer, BoardSerializer


class ListNewsView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class ListBoardView(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

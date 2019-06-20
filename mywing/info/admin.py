from django.contrib import admin
from mywing.info.models import News, Board, BoardSnapshot, BoardSnapshotItem


admin.site.register(News)
admin.site.register(Board)
admin.site.register(BoardSnapshot)
admin.site.register(BoardSnapshotItem)

from django.contrib import admin
from .models import Round, Board, ScoreBoard

# Register your models here.
@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):
    fields = ("board", "winning_slot", "winning_seed", "title", "description", "lock_time")

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(ScoreBoard)
class ScoreAdmin(admin.ModelAdmin):
    exclude = ()
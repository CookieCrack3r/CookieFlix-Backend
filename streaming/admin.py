from django.contrib import admin
from .models import Video, Category

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'uploaded_at', 'category', 'display_users')
    search_fields = ('title',)
    
    def display_users(self, obj):
        return ", ".join([user.email for user in obj.users.all()])
    display_users.short_description = 'Benutzer'
    
    def has_add_permission(self, request):
        return request.user.is_superuser

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

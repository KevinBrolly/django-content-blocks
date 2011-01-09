from content_blocks.models import Block
from django.contrib import admin

class BlockAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'template_position')
    
    search_fields = ['title']
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'template_position', None) is not Block.NO_POSITION:
            Block.objects.filter(template_position=obj.template_position).update(template_position=Block.NO_POSITION)
        
        obj.save()
    
admin.site.register(Block, BlockAdmin)

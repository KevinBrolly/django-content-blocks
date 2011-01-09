from django import template
from content_blocks.models import Block

register = template.Library()

class BlockNode(template.Node):
    def __init__(self, block_name):
        self.block_name = block_name
    def render(self, context):
        try:
            block = Block.objects.get(template_position=self.block_name)
        except:
            block = None
        context['block'] = {self.block_name: block}
        return ''

def get_block(parser, token):
    try:
        tag_name, block_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]
    if not (block_name[0] == block_name[-1] and block_name[0] in ('"', "'")):
        raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
    return BlockNode(block_name[1:-1])

register.tag('get_block', get_block)

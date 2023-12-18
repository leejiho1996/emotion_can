import markdown
from django import template
from django.utils.safestring import mark_safe
register = template.Library()


@register.filter # 애터네이션 적용하면 템플릿에서 해당 함수 사용가능
def sub(value, arg):
    return value - arg

@register.filter
def mark(value):
    extensions = ['nl2br', 'fenced_code'] #nl2br은 줄바꿈 문자를 <br> 로 바꾸어 준다. fenced_code는 마크다운의 소스코드 표현을 위해 필요.
    return mark_safe(markdown.markdown(value, extensions=extensions))

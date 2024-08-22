from django import template

from todoist.models import Todo

register = template.Library()


@register.filter
def toggle_status_label(status):
    if status == Todo.Status.DONE:
        return "Mark not Done"
    elif status == Todo.Status.NOT_DONE:
        return "Mark Done"

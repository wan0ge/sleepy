# coding: utf-8
from logging import getLogger

from flask import Request

from plugin import Plugin, StatusUpdatedEvent

l = getLogger(__name__)
p = Plugin(
    'test2',
    require_sleepy_version=((6, 0, 0), (7, 0, 0))
)

p.init = lambda: l.debug('test2 loaded')


@p.event_handler(StatusUpdatedEvent)
def set_event_handler(event: StatusUpdatedEvent, request: Request):
    if event.new_status == 123:
        event.intercept('intercepted')
    elif event.new_status == 114514:
        event.new_status = p.global_data.get_status(1919810)[1]
    elif 'test2' in request.args:
        event.new_status = p.global_data.get_status(999999)[1]
    return event

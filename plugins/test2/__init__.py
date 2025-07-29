# coding: utf-8
from logging import getLogger

from flask import Request

from plugin import Plugin, StatusUpdatedEvent

l = getLogger(__name__)
p = Plugin('test2')

p.init = lambda: l.debug('test2 loaded')


@p.event_handler(StatusUpdatedEvent)
def set_event_handler(event: StatusUpdatedEvent, request: Request):
    if event.new_status == 123:
        event.intercept('intercepted')
    elif event.new_status == 114514:
        event.new_status = 1919810
    elif 'test2' in request.query_string.decode():
        event.new_status = 999999
    return event

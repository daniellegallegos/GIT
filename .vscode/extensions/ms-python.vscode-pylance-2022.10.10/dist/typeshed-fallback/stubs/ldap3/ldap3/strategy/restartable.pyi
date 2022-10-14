from typing import Any

from .sync import SyncStrategy

class RestartableStrategy(SyncStrategy):
    sync: bool
    no_real_dsa: bool
    pooled: bool
    can_stream: bool
    restartable_sleep_time: Any
    restartable_tries: Any
    exception_history: Any
    def __init__(self, ldap_connection) -> None: ...
    def open(self, reset_usage: bool = ..., read_server_info: bool = ...) -> None: ...
    def send(self, message_type, request, controls: Any | None = ...): ...
    def post_send_single_response(self, message_id): ...
    def post_send_search(self, message_id): ...
    def get_stream(self) -> None: ...
    def set_stream(self, value) -> None: ...

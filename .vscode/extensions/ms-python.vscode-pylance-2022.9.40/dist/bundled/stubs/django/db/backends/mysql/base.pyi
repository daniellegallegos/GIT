import sys
from typing import Any, Dict, Optional, Type

from django.db.backends.base.base import BaseDatabaseWrapper as BaseDatabaseWrapper

from .client import DatabaseClient
from .creation import DatabaseCreation
from .features import DatabaseFeatures
from .introspection import DatabaseIntrospection
from .operations import DatabaseOperations
from .validation import DatabaseValidation

if sys.version_info < (3, 8):
    from typing_extensions import Literal
else:
    from typing import Literal

version: Any
django_conversions: Any
server_version_re: Any

class CursorWrapper:
    codes_for_integrityerror: Any = ...
    cursor: Any = ...
    def __init__(self, cursor: Any) -> None: ...
    def execute(self, query: Any, args: Optional[Any] = ...): ...
    def executemany(self, query: Any, args: Any): ...
    def __getattr__(self, attr: Any): ...
    def __iter__(self) -> Any: ...

class DatabaseWrapper(BaseDatabaseWrapper):
    client: DatabaseClient
    creation: DatabaseCreation
    features: DatabaseFeatures
    introspection: DatabaseIntrospection
    validation: DatabaseValidation
    ops: DatabaseOperations

    client_class: Type[DatabaseClient]
    creation_class: Type[DatabaseCreation]
    features_class: Type[DatabaseFeatures]
    introspection_class: Type[DatabaseIntrospection]
    ops_class: Type[DatabaseOperations]
    validation_class: Type[DatabaseValidation]

    vendor: str = ...
    data_types: Any = ...
    operators: Any = ...
    pattern_esc: str = ...
    pattern_ops: Any = ...
    isolation_levels: Any = ...
    Database: Any = ...
    SchemaEditorClass: Any = ...
    isolation_level: Any = ...
    def get_connection_params(self) -> Dict[str, Any]: ...
    def get_new_connection(self, conn_params: Any): ...
    def init_connection_state(self) -> None: ...
    def create_cursor(self, name: Optional[Any] = ...): ...
    def disable_constraint_checking(self) -> Literal[True]: ...
    needs_rollback: Any = ...
    def enable_constraint_checking(self) -> None: ...
    def check_constraints(self, table_names: Optional[Any] = ...) -> None: ...
    def is_usable(self) -> bool: ...
    @property
    def display_name(self) -> str: ...  # type: ignore
    @property
    def data_type_check_constraints(self): ...
    @property
    def mysql_server_data(self) -> Dict[str, Any]: ...
    @property
    def mysql_server_info(self): ...
    @property
    def mysql_version(self): ...
    @property
    def mysql_is_mariadb(self): ...
    @property
    def sql_mode(self): ...
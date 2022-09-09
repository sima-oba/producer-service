from enum import Enum


class Role(Enum):
    ADMIN = 'admin'
    READ_PROPERTIES = 'read-properties'
    WRITE_PROPERTIES = 'write-properties'
    MANAGE_PROPERTIES = 'manage-properties'

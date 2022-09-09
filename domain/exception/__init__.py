class EntityNotFoundError(Exception):
    def __init__(self, entity, reason: str):
        if hasattr(entity, '__name__'):
            entity = entity.__name__

        super().__init__(f'Entity {entity} not found: {reason}')


class InvalidStateError(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidValueError(Exception):
    def __init__(self, message):
        super().__init__(message)

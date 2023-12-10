from typing import Final


class EventErrors:
    NOT_USERS_LOCATION: Final[str] = 'У пользователя нет такого адреса'
    NOT_USERS_CHILD: Final[str] = 'У пользователя нет такого ребёнка'
    FINISH_TIME_BEFORE_START_TIME: Final[str] = 'Окончание должно быть позже начала'

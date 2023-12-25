import os
from typing import ClassVar, List, NamedTuple

class Social(NamedTuple):
    do_send: bool
    obj: str
    name: str

class Socials:
    _telegram = Social(
        do_send=bool(os.getenv('USE_TELEGRAM', True)),
        obj='telegram_post',
        name='telegram'
    )

    _all_socials: ClassVar[List[Social]] = [_telegram]  # Fix: Corrected the reference to _telegram

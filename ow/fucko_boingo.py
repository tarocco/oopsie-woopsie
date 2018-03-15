from .fucky_wucky import FuckyWucky
from .oopsie_woopsie_exception import OopsieWoopsieException
from .size import Size

class FuckoBoingo(FuckyWucky):
    def __init__(self, size):
        super(FuckoBoingo, self).__init__(size)
        # We cannot have any wittle fucko boingos!! uwu
        if not isinstance(size, Size) or size == Size.WITTLE:
            raise OopsieWoopsieException(self)

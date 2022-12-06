class MultiSelectEntry:
    TICK_EMOJI = "<:GreenTick:1046209589470822450>"
    CROSS_EMOJI = "<:RedCross:1046847127504044072>"
    BACK_EMOJI = "⏪"
    FORWARD_EMOJI = "⏩"
    DOWN_EMOJI = "⬇"
    UP_EMOJI = "⬆"

    def __init__(self, data, display_name, options):
        self.data = data
        self.display_name = display_name
        self.options = options
        self.option = self.options[0]
        self.is_complete = False

    def __str__(self):
        return f"{self.display_name}\t{self.__class__.TICK_EMOJI if self.is_complete else self.__class__.CROSS_EMOJI}"

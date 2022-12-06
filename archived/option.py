class Option:
    TICK_EMOJI = "<:GreenTick:1046209589470822450>"
    CROSS_EMOJI = "<:RedCross:1046847127504044072>"
    TOGGLE_EMOJI = "<:ToggleOption:1047629772387262484>"
    BACK_EMOJI = "⏪"
    FORWARD_EMOJI = "⏩"

    def __init__(self, name, display_value, value):
        self.name = name
        self.value = value
        self.display_value = display_value
        self.is_selected = False

    def __str__(self):
        return f"{self.name}\t{self.__class__.TICK_EMOJI if self.is_selected else self.__class__.CROSS_EMOJI}"

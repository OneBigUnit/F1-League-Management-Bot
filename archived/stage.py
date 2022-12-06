class Stage:
    TICK_EMOJI = "<:GreenTick:1046209589470822450>"
    CROSS_EMOJI = "<:RedCross:1046847127504044072>"
    BACK_EMOJI = "⏪"
    FORWARD_EMOJI = "⏩"

    def __init__(self, name, description, f, default_value, optional=False):
        self.name = name
        self.description = description
        self.f = f
        self.optional = optional
        self.is_complete = False
        self.value = default_value
        self.default_value = default_value

    def __str__(self):
        return f"{self.name}\t{'(Optional)' if self.optional else ''}\t" \
               f"{self.__class__.TICK_EMOJI if self.is_complete else self.__class__.CROSS_EMOJI}"

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

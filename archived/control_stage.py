class ControlStage:
    TICK_EMOJI = "<:GreenTick:1046209589470822450>"
    CREATE_EMOJI = "<:NewEntry:1047502950660046861>"
    DELETE_EMOJI = "🗑️"

    def __init__(self, description, f, update_method):
        self.description = description
        self.f = f
        self.do_updates = update_method

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

class Dialog:

    def __init__(self, updated_intent):
        self._type = "Dialog.Delegate"
        self._updated_intent = updated_intent

    def build(self):
        return {
            "type": self._type,
            "updatedIntent": self._updated_intent
        }

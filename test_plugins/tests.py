class TestModule(object):
    def tests(self):
        return {
            'bool': self.is_bool,
        }

    def is_bool(self, value):
        return isinstance(value, bool)

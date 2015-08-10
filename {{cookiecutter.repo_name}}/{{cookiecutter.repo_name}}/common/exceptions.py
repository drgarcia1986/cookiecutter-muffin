

class ErrorListBase(Exception):

    def __init__(self, errors):
        self.errors = errors
        if not isinstance(self.errors, list):
            self.errors = [self.errors]


class ValidationError(ErrorListBase):
    pass


class ProcessError(ErrorListBase):
    pass

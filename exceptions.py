class Signal(Exception):
    pass

class RestartSignal(Signal):
    pass

class TerminateSignal(Signal):
    pass
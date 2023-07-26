class AppIDNoneError( Exception ):
    pass

class WrongArgumentError( Exception ):
    pass


def create_error_message(message):
    return f"\n========================   Error Message   =========================\n{message}\n"
# Arquivo que verifica ataques de SQLInjection

def antiSQLInjection(string: str) -> bool:
    chars = [' ', ';', '>', '<', ';', ':']
    return any(char in string for char in chars)
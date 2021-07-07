class CommandDoesntExists(Exception):
    '''
    Usado quando o usuário passar um comando diferente de:
        - CUMP
        - LIST
        - PEGA
        - TERM
    '''

class UsernamePasswordNotMatch(Exception):
    description: str = 'Occurs when Username or Password does not match'

    def __str__(self):
        return "Username or Password does not match"

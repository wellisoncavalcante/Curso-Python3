# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# Usar as funções decoradoras em outras funções.

def create_function(func):
    def internal(*args, **kwargs):
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        return result
    return internal

def invert_function(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverted = invert_function('Wellison')
print(inverted)
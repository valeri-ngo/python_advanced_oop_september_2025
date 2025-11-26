def tags(param_type):

    def decorator(func):

        def wrapper(*args, **kwargs):
            
            return f'<{param_type}>{func(*args, **kwargs)}</{param_type}>'
        
        return wrapper
    
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
print()
@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
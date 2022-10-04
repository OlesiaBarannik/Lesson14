def stop_words(words: list):
    def inner(func):
        def wrapper(name):
            str = func(name)
            for v in words:
                str = str.replace(v, "*")
            return str

        return wrapper

    return inner

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"
print(create_slogan("Samvel"))

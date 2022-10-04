def arg_rules(type_: type, max_length: int, contains: list):
    def inner(func):
        def wrapper(name):
            erorr = []
            if type(name) != str:
                erorr.append("type error")

            if len(name) >= max_length:
                erorr.append("length error")

            for i in contains:
                if i not in name:
                    erorr.append("contains error")
                    break

            if len(erorr) > 0:
                print(erorr)
                return False
            else:
                print(func(name))
                return True

        return wrapper

    return inner

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
print(create_slogan(("11110511@")))



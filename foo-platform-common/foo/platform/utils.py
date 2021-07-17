from foo.core.foo_core import bar

def baz() -> None:
    print("I'm in baz, about to bar():")
    bar()
    print("Done with that.")

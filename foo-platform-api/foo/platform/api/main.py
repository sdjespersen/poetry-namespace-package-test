from foo.core.foo_core import bar
from foo.platform.utils import baz

def main() -> None:
    print("Here we are in API main, next calling bar() directly:")
    bar()
    print("Okay back in main, going to call baz() now:")
    baz()
    print("All done with main.")

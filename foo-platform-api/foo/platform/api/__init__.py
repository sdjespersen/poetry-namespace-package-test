# Notice how this init file is nested more deeply than in foo.core. This is
# because foo.platform.api shares the common prefix foo.platform with at least
# one other package (specifically, foo.platform.common). Thus to prevent
# conflicts, neither foo/__init__.py nor foo/platform/__init__.py may be
# present!

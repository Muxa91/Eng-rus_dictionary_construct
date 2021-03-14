import textwrap


x = """foo bar
    baz
    foobar
    foobaz
    """

x=textwrap.fill.shorten(x, width=99999999999)
print(x)
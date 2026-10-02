basic.show_leds("""
    . . # . .
    . # # # #
    # # # # #
    . # # # #
    . . # . .
    """)

def on_forever():
    basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        . # # # .
        . # # # .
        """)
basic.forever(on_forever)

def on_forever2():
    basic.show_leds("""
        . . # . .
        # # # # .
        # # # # #
        # # # # .
        . . # . .
        """)
basic.forever(on_forever2)

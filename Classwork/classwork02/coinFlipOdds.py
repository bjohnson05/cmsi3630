#
# A command line application that reports the odds of tossing a fair coin 1-10
# times and getting heads each time.
#

# We'll show odds both in "1 in n" format and in percentage format
message = "Odds of throwing {0:4d} heads in a row is 1 in {1:7d} ({2:8.5f}%)"

possibilities = 2
for tosses in range( 1, 51 ):
    percentage = 100.0 / possibilities
    line = message.format( tosses, possibilities, percentage )
    print( line )

    # Ready for the next iteration
    possibilities *= 2

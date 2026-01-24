# Day 3: Lobby

## Part 1

My line of thinking for this was straightforward, find the first largest digit from the line and take the index of that digit. Then find the next largest digit in the line starting from just after the index of the first one. The first one also could not be the last digit in the string.

## Part 2

Part 2 made this a bit more difficult. I was quickly able to revise the algorithm to loop over a range and look through subsections of each line. I did make a mistake while redefining the starting index for the search. I had made it look for the first instance of a value when I needed to look for the first instance starting at the last starting index. Once fixed, the answer came forth and sent me onto day 4.
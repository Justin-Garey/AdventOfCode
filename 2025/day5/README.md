# Day 5

## Part 1

All I did was create a list of numbers based on the provided ranges, then check if the later values were in the consolidated list. Then I found out that wouldn't work for the actual input so I created a list for the range tuples (start, end) then checked if the value was within any ranges. This resulted in a much faster and working solution.

## Part 2

This was more complicated than I initially thought. I ended up creating a recursive function to add ranges to a saved ranges list. The function basically checked each new range to see if it could fit in to the existing list without overlap and if there was overlap, then we could modify the range and call the add range function again. 
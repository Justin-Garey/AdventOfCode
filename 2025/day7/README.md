# Day 7

## Part 1

This one was fun. I looped over the input line by line keeping track of what I saw and whether a beam was continued or not. It helped to graphically display the mapped paths just like the example.

## Part 2

This was much more complicated than I initially thought it would be. I first created a recursive function to take the map I had and count the paths from each node. That worked for the example but was not feasible for the actual input. Then I switched to keeping count of possible paths in the map from solution 1. I was unable to get this part myself. I ended up looking up a visualization of the problem and found I had an addition issue. The path count prior to hitting a splitter needs duplicated to each side, not just kept on one with the other side having 1 possibility. Fixing that immediately gave me the answer.
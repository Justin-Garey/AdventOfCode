# Day 6

## Part 1

I started this by turning the input into a 2d array with the same format, then I could loop over each column. The loop grabbed the operator first, then looped again, grabbing each element within the column to apply to the math problem.

## Part 2

This problem threw me through a loop at first. I had to reread the instructions a few times to wrap my head around "Cephalopod math" but eventually I got it. Once I understood how the math worked, I completely trashed the first solution and restarted since the spacing was crucial to how the math worked. I created columns of the characters then reversed it so we could work in order. Columns then got appended together and when an operator appeared, the appended numbers were used to find an individual solution to add to the sum total. 
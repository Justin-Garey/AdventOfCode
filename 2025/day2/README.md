# Day 2: Gift Shop

## Part 1

I first misread the instructions today and started off only checking the first an last numbers in a sequence instead of generating the sequence. This challenge felt simpler today. The first part was solvable by looping over the sequences checking if the first half was equal to the second half, and if so, adding the integer value to the total.

## Part 2

I felt accomplished after getting this one on my first try today. I started by modifying my algorithm to keep the old functionality for even length ids and for the odd ones, I would find a list of integers that could multiply to the length. With that list, I would check each multiplier until one I found was the length of a repeated sequence. This sort of worked until I got rid of the even vs. odd functionality and only used this multiplier checker. At last, the answer was mine and I could go further into my journey of helping the North Pole.
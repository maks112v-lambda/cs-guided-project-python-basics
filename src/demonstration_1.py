"""
Define a function that transforms a given string into a new string where the
original string was split into strings of a specified size.

For example:
If the input string was this:

"supercalifragilisticexpialidocious"

and the specified size was 3, then the return string would be:

"sup erc ali fra gil ist ice xpi ali doc iou s"

The assumptions we are making about our input are the following:

- The input string's length is always greater than zero.
- The string has no spaces.
- The specified size is always a positive integer.
"""
def split_in_parts(s, part_length):
    output = []
    counter = 0
    for char in s:
        counter += 1
        if counter % part_length == 0:
            output.append(char)
            output.append(" ")
        else:
            output.append(char)
    return output
# Your code here
arr_to_print = split_in_parts("supercalifragilisticexpialidocious", 3)
print("".join(arr_to_print))

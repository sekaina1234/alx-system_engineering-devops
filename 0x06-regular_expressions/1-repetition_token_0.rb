#!/usr/bin/env ruby

def repetition_token_0(input_string)
  # Regular expression to match the pattern with repetition token {0}
  pattern = /hbt{0}n/

  # Use the match method to find matches in the input_string
  matches = input_string.scan(pattern)

  # Print the matches found
  puts matches.join
end

# Taking the argument from the command line
input_argument = ARGV[0]

# Calling the method to find and print matches for the regular expression
repetition_token_0(input_argument)

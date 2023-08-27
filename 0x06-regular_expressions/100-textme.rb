#!/usr/bin/env ruby

def find_and_print_pattern_occurrences(input_string)
  occurrences = input_string.scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/)
  result = occurrences.map { |match| match.join(',') }
  puts result.join(',')
end

# Taking the argument from the command line
input_argument = ARGV[0]

# Calling the function to find and print occurrences of the pattern
find_and_print_pattern_occurrences(input_argument)
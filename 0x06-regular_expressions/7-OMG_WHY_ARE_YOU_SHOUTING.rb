#!/usr/bin/env ruby

def find_and_print_uppercase_letters(input_string)
  occurrences = input_string.scan(/[A-Z]/)
  puts occurrences.join
end

# Taking the argument from the command line
input_argument = ARGV[0]

# Calling the function to find and print occurrences of uppercase letters
find_and_print_uppercase_letters(input_argument)

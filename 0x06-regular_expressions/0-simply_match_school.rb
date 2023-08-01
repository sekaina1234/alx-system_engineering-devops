#!/usr/bin/env ruby
def find_and_print_school_occurrences(input_string)
  occurrences = input_string.scan(/School/)
  puts occurrences.join
end
input_argument = ARGV[0]
find_and_print_school_occurrences(input_argument)

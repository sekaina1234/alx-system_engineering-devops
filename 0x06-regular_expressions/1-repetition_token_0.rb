#!/usr/bin/env ruby
def find_and_print_pattern_occurrences(input_string)
  occurrences = input_string.scan(/hbt{2,5}n/)
  puts occurrences.join
end
input_argument = ARGV[0]
find_and_print_pattern_occurrences(input_argument)

#!/usr/bin/env ruby
def repetition_token_0(input_string)
  pattern = /hbt{0}n/
  matches = input_string.scan(pattern)
  puts matches.join
end
input_argument = ARGV[0]
repetition_token_0(input_argument)

#!/usr/bin/env ruby

# Check if the script is invoked with an argument
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Get the input string from the command line argument
input_string = ARGV[0]

# Define the regular expression pattern to match "School"
pattern = /School/

# Perform the regular expression matching
if (match = input_string.match(pattern))
  puts match[0]
else
  puts ""
end

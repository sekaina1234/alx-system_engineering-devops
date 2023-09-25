# Define SSH client configuration file path
$ssh_config_file = '/etc/ssh/ssh_config'

# Ensure the SSH client configuration file is present
file { $ssh_config_file:
  ensure => file,
}

# Disable password authentication in SSH client configuration
file_line { 'Turn off passwd auth':
  path   => $ssh_config_file,
  line   => 'PasswordAuthentication no',
}

# Declare the identity file to use for SSH connections
file_line { 'Declare identity file':
  path   => $ssh_config_file,
  line   => 'IdentityFile ~/.ssh/school',
}

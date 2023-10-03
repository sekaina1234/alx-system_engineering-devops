# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Define a custom fact to get the server's hostname
Facter.add('custom_hostname') do
  setcode 'hostname'
end

# Create a custom configuration file for Nginx
file { '/etc/nginx/sites-available/custom_header':
  ensure  => 'present',
  content => "server {\n"
             "  listen 80 default_server;\n"
             "  server_name _;\n"
             "  location / {\n"
             "    add_header X-Served-By $custom_hostname;\n"
             "    proxy_pass http://backend;\n"
             "  }\n"
             "}\n",
}

# Create a symbolic link to enable the custom configuration
file { '/etc/nginx/sites-enabled/custom_header':
  ensure => 'link',
  target => '/etc/nginx/sites-available/custom_header',
  notify => Service['nginx'],
}

# Restart Nginx to apply the configuration
service { 'nginx':
  ensure  => 'running',
  enable  => 'true',
  require => File['/etc/nginx/sites-enabled/custom_header'],
}


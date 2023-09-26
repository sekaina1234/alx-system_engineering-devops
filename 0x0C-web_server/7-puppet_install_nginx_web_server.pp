# Define a class for Nginx installation and configuration
class web_server {

  # Install Nginx package
  package { 'nginx':
    ensure => 'installed',
  }

  # Ensure Nginx service is enabled and running
  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
  }

  # Create a custom 404 error page
  file { '/var/www/html/custom_404.html':
    ensure  => file,
    content => 'Ceci n\'est pas une page',
    require => Package['nginx'],
  }

  # Define the Nginx configuration file
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('web_server/nginx.conf.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Create a symbolic link to enable the custom 404 page site
  file { '/etc/nginx/sites-enabled/default':
    ensure => link,
    target => '/etc/nginx/sites-available/default',
  }
}

# Define the main node and include the web_server class
node 'default' {
  include web_server
}

# Define the Nginx configuration template
file { '/etc/nginx/sites-available/default':
  content => template('web_server/nginx.conf.erb'),
}

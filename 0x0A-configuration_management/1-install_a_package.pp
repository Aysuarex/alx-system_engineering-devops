# Installs flask from pip3 using Puppet

exec { 'install flask':
  command => 'sudo pip3 install flask',
  path    => '/usr/bin',
  }

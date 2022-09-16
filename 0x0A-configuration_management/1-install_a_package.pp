# Installs flask from pip3

exec { 'install flask':
  command => 'pip3 install flask',
  path => ['/usr/bin']
}

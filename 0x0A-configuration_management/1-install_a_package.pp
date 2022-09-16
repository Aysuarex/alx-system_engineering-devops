# Installs flask from pip3 using Puppet

package { 'flask':
    ensure => 'present',
    command => 'pip3 install flask flask_restful apiai',
    path => ['/usr/bin'],
    unless => '/usr/bin/test -f /usr/local/lib/python3.4/dist-packages/flask/app.py'
}

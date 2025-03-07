# Script to increase the amount of traffic an Nginx Server can handle
# Increase the ULIMIT of the default file

exec {
    'increase_nginx_ulimit':
        command => 'sed -i "s/15/4096/" /etc/default/nginx',
        path    => '/usr/bin:/usr/sbin:/bin'
}

-> exec { 'restart_ngnix':
    command => 'service nginx restart',
    path    => '/usr/bin:/usr/sbin:/bin'
}

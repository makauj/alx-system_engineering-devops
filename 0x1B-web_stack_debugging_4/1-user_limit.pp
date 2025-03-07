# script to change OS config so you can login with Holberton
# and open a file without errors

exec { 'change_os_config':
  command => 'sed -i "/holberton hard/s/5/50000/g" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/usr/bin/',
}

exec { 'change_os_config2':
  command => 'sed -i "/holberton soft/s/5/50000/g" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/usr/bin/',
}

# Puppet script to fix Apache 200 error on a Wordpress website
# fix faulty worpress website

exec { 'fix_apache_200_error':
  command => 'bash -c "sed -i s/class-wp-locale.phpp/class-wp-locale.php/g \
/var/www/html/wp-settings.php; service apache2 restart"',
  path    => '/usr/bin:/usr/sbin:/bin'
  }

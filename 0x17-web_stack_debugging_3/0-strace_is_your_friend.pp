# Puppet script to fix Apache 500 error on a Wordpress website
# fix faulty worpress website

exec { 'fix_apache_500_error':
  command => 'bash -c "sed -i s/class-wplocale.phpp/class-wp-locale.php/ \
  /var/www/html/wp-settings.php && service apache2 restart"',
  path    => '/usr/bin:/usr/sbin:/bin'
}

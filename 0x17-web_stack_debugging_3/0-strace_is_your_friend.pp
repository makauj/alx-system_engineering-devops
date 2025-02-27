# Puppet script to fix Apache 200 error on a Wordpress website
# fix faulty worpress website

$error_file = '/var/www/html/wp-settings.php'
exec { 'fix_apache_200_error':
  command => 'sed -i "s/phpp/php/g" $error_file',
  path    => '/usr/bin:/usr/sbin:/bin'
  }

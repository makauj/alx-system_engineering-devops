#Puppet script to create ssh config file

$file_content = file('/etc/ssh/ssh_config')
$config = "${file_content}\
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
"
file {  'school':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',  # Ensure this is for the correct user
  content => $config
}

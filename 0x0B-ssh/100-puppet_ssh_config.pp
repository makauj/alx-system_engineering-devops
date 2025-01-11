#Puppet script to create ssh config file

file { 'ssh_config':
  ensure  => 'file',
  path    => '/home/ubuntu/.ssh/config',  # Ensure this is for the correct user
  owner   => 'ubuntu',                    # Ensure the file is owned by the user (change if needed)
  group   => 'ubuntu',                    # Group of the user (change if needed)
  mode    => '0600',                      # Ensure the file is read/write only for the user
  content => "Host *\n" +
             "    IdentityFile ~/.ssh/school\n" +
             "    PasswordAuthentication no\n",
}

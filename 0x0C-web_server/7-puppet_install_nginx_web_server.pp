# To install & configure nginx on a server using Puppet

$config = "server {
	listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html;

        location /redirect_me {
                return 301 https://www.makau.tech;
        }
}"
# install nginx server
package { 'nginx':
ensure	=> 'installed',
}

file { 'index.html':
ensure	=> 'present',
path	=> '/var/www/html/index.html',
content	=> 'Hello World!',
mode	=> '0644'
}

file { 'server_config':
ensure	=> 'present',
path 	=> '/etc/nginx/sites-available/default',
content => $config
}

exec { 'service nginx restart':
path	=> ['/usr/sbin', '/usr/bin']
}

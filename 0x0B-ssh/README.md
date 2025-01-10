# 0x0B. SSH

## Learning Objectives

- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`

## Tasks

0. Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

Requirements:

    - Only use ssh single-character flags
    - You cannot use -l
    - You do not need to handle the case of a private key protected by a passphrase

1. Write a Bash script that creates an RSA key pair.

Requirements:

- Name of the created private key must be school
- Number of bits in the created key to be created 4096
- The created key must be protected by the passphrase betty
Example:
```
sylvain@ubuntu$ ls
1-create_ssh_key_pair
sylvain@ubuntu$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in school.
Your public key has been saved in school.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key's randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
sylvain@ubuntu$ ls
1-create_ssh_key_pair school  school.pub
sylvain@ubuntu$ 
```

2. Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:

- Your SSH client configuration must be configured to use the private key ~/.ssh/school
- Your SSH client configuration must be configured to refuse to authenticate using a password

3. Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the ubuntu user.
```ssh key
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
```

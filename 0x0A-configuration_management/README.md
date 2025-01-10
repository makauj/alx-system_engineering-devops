# 0x0A. Configuration management

## Tasks

0. Using Puppet, create a file in /tmp.

    Requirements:

    - File path is `/tmp/school`
    - File permission is `0744`
    - File owner is `www-data`
    - File group is `www-data`
    - File contains `I love Puppet`

    **code**
    - Use `ensure` to ensure file `/tmp/school` exists
    - specify content in the file using `content`
    - give permissions using `mode`
    - Set the owner of the file using `owner`
    - Set the group of the file using `group`

1. Using Puppet, `install` flask from `pip3`.

    Requirements:

    - Install `flask`
    - Version must be `2.1.0`

    **Code**
    - Check that `flask v2.1.0` will be installed installed using `ensure`
    - Tell Puppet to use 'pip' ti install package using `provider`
    - specify the name of the package using `source`
    - If a different version is already installed, upgrade it to the specified version using `install_options => ['--upgrade']`

2. Using Puppet, create a manifest that kills a process named killmenow.

    Requirements:

    - Must use the `exec` Puppet resource
    - Must use `pkill`
    Example:

    - Terminal #0 - starting my process

    **Code**
    - Use `command` to give the command to kill process
    - Ensure the command will only run if `killmenow` is currently runing using `unless`
    - specify the path using `path => ['/usr/bin', '/bin']`

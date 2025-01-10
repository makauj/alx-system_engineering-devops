package { 'flask':
    ensure          => '2.1.0',
    provider        => 'pip',
    source          => 'flask',
    install_options => ['--upgrade'],
}

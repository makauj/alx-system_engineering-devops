#Manifest that kills a process named `killmenow`
exec { 'kill_killmenow_process':
  command => 'pkill killmenow',
  unless  => 'pgrep killmenow',
  path    => ['/usr/bin', '/usr/bin'],
}

exec { 'kill_killmenow_process':
  command => 'pkill killmenow',
  unless  => 'pgrep killmenow',
  path    => ['/usr/bin', '/bin'],
}

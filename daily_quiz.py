command_table = {'journalctl': '-ef',
                 'journalctl': 'systemd_unit=<service>',
                 'journalctl': '-u <daemon>.service',
                 'journalctl': '-p <term>',
                 'journalctl': '-b -<n>',
                 'journalctl': '--since <yyyy-mm-dd>  --until <yyyy-mm-dd>',
                 'journalctl': '-o verbose'
                 }
print (command_table.items())

logs_to_view {'/run/log/journal': 'system journal',
              '/var/log/journal': 'persistent logging'}

#making a persistent journal
# mkdir -> chown -> chmod -> reboot (killall -USR1 systemd-journald


#/etc/sysconfg/<service_mname>  |  main config files for servies
#systemd.journal-fields
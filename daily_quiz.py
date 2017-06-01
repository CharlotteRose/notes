


command_table = {'journalctl7': '-ef',
                 'journalctl6': 'systemd_unit=<service>',
                 'journalctl5': '-u <daemon>.service',
                 'journalctl4': '-p <term>',
                 'journalctl3': '-b -<n>',
                 'journalctl2': '--since <yyyy-mm-dd>  --until <yyyy-mm-dd>',
                 'journalctl1': '-o verbose'
                 }
for i in command_table:
        print(i, command_table[i])

#logs_to_view {'/run/log/journal': 'system journal',
 #             '/var/log/journal': 'persistent logging'}
error = '1' #will be rand num | static for testing now
#making a persistent journal
#def get_topic_(

# mkdir -> chown -> chmod -> reboot (killall -USR1 systemd-journald
Htppd_logs=['/var/log/httpd/access_log' ,'/var/log/httpd/error_log']
print (Htppd_logs.__len__())
#/etc/sysconfg/<service_mname>  |  main config files for servies
#systemd.journal-fields
answer = input("If unable to use a web browser which command line tool\n"
               "would you use to view the contents of a web page?")
answer = answer.lower() # optimized way to have input lowered upon entry?
print (answer)
#one option is use reference aprops to see similar commands

#file_permissions
#per
#SHOULD BE ABLE TO VIEW FILE OF MAN PAGE -> groff typesetting is used -> .SH *should* denote header or section header

#Commands to include
#ausearch
#curl, elinks

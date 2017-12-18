"""
    This module is for using Linux.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

terminal_context = AppContext(executable="MobaXterm_Personal_7.4")
putty_context = AppContext(executable="putty")
cmder_context = AppContext(executable="cmder")
octave = AppContext(executable="octave-gui")
grammar = Grammar("linux", context=(terminal_context | putty_context | cmder_context | octave))

linux_rule = MappingRule(
    name="linux",
    mapping={

# Linux --------------------------------------------------------------------------------------
            "[linux] clear [terminal]":                   Text("clear") + Key("enter"),                         # clear
            "[linux] (run | repeat) [the] last command":  Text("!!") + Key("enter"),                            # Repeat last command used.
            "[linux] (run | repeat) [the] last [command] as sudo": Text("sudo !!") + Key("enter"),              # Repeat last command used as sudo.
            "[linux] create tar":                         Text("tar -xvzf "),                                   # tar -cvzf <filename>.tgz directory                          | Compress the contents of an archive in the tar format.
            "[linux] (tar | unpack)":                     Text("tar -cvzf "),                                   # tar -xvzf /path/to/yourfile.tgz                             | x for extract, v for verbose, z for gnuzip, f for file, should come last just before file name.
            "[linux] unzip":                              Text("unzip "),                                       # unzip <filename>.zip                                        | Extract files and directories from a compressed zip archive.
            "[linux] ping google":                        Text("ping -c 3 google.com") + Key("enter"),          # Check to see if you can access a website like Google.
            "[linux] (W get | web get)":                  Text("wget "),                                        # wget <http://example.com/file.txt>                          | Download files from the web directly, download straight into the current directory.
        # Vocabulary
            "[linux] apt":                                Text("apt "),
            "[linux] apt get":                            Text("apt-get "),
            "linux linux":                                Text("linux "),
            "linux sudo":                                 Text("sudo "),
        # Man
            "linux man":                                  Text("man "),                                         # Reference manuals.
            "[linux] man search":                         Text("/"),                                            # Search once in man.
            "[linux] man next":                           Text("n"),                                            # Search next.
            "[linux] man up":                             Text("N"),                                            # Search up.
            "[linux] where is":                           Text("whereis "),                                     # whereis <command_name>                                      | Will display the documentation, binaries and source files of a specific command.
        # History
            "[linux] (history | show last) <n>":          Text("history %(n)d") + Key("enter"),                 # See <n> recently typed commands.
            "[linux] (history (all | list) | [show] history)": Text("history") + Key("enter"),                  # See recently typed commands.
            "[linux] history less":                       Text("history | less") + Key("enter"),                # See recently typed commands in less text editor.
            "[linux] (history (C | clear | delete) | (clear | delete) history)": Text("history -c") + Key("enter"), # Clear the history list. This may be combined with the other options to replace the history list completely.
            "[linux] (history (W | write | save) | (write | save) history)": Text("history -w") + Key("enter"), # Write out the current history list to the history file.
            "[linux] (history C W | [history] clear and write [history])": Text("history -c -w") + Key("enter"), # Clear and write history.
            "[linux] [history] (execute | repeat) <n>":   Text("!%(n)d") + Key("enter"),                        # Recall and execute commands by <n> reference.
            "[linux] [history] ([execute] last command | repeat last)": Text("!!") + Key("enter"),              # Re-execute the previous command.
            "[linux] [history] insert last command":      Text("!! "),                                          # Substitute the most recent command and execute, e.g. sudo !! (will insert previous command after sudo).
            "[linux] sudo (repeat | bang)":               Text("sudo !!"),                                      # Repeat the last command with sudo.
        # Users
            "[linux] (add | [create] new) user":          Text("sudo adduser "),                                # adduser <name>                                              | Add a user. You will need to use passwd to sign a password to the account.
            "[linux] (add | [create] new) group":         Text("sudo groupadd "),                               # groupadd <name>                                             | Create a new group with the options that you give it.
            "[linux] change (owner | ownership)":         Text("sudo chown "),                                  # chown [OPTION]... [OWNER][:[GROUP]] FILE...                 | Change the user and/or group ownership of each given file or directories.
            "[linux] change (owner | ownership) recursively": Text("sudo chown -R "),                           # chown -R [OWNER][:[GROUP]] FILE...                          | Change the user and/or group ownership of each given file or directories, operate on files and directories recursively.
            "[linux] change password":                    Text("passwd "),                                      # passwd <name>                                               | Change user password.
            "[linux] delete user":                        Text("sudo userdel "),                                # userdel <name>                                              | Delete a user.
            "[linux] delete user and files":              Text("sudo userdel -r "),                             # userdel -r <name>                                           | Delete a user and all the files the user created.
            "[linux] lock user account":                  Text("usermod -L "),                                  # usermod -L <name>                                           | Lock user account.
            "[linux] unlock user account":                Text("usermod -U "),                                  # usermod -U <name>                                           | Unlock user account.
            "[linux] give user sudo permissions":         Text("usermod -aG sudo "),                            # usermod -aG sudo <name>                                     | Give user sudo permissions.
            "[linux] switch user":                        Text("su "),                                          # su <name>                                                   | Add a user.
            "[linux] who am I":                           Text("whoami") + Key("enter"),                        # Which user am I.
            "[linux] who is logged on":                   Text("who") + Key("enter"),                           # List all the users that are currently logged in and any other useful information about the logged in users.
            "[linux] recently logged in":                 Text("last") + Key("enter"),                          # Shows a list of users who have recently been logged in.
        # System
            "([linux] time (now | and date) | what time is it)": Text("date") + Key("enter"),                   # Server date and time right now.
            "[linux] (dee F | disk space usage)":         Text("df") + Key("enter"),                            # Report file system disk space usage.
            "[linux] (dee F H | disk space usage readable)": Text("df -h") + Key("enter"),                      # Report file system disk space usage, and print sizes in human readable format.
            "[linux] (error debug | find errors)":        Text("grep -Ei 'WARN|CRITICAL|FATAL' /var/log/{syslog,journalctl}") + Key("enter"), # Colorized incensitive multi grep. Finds errors without having to grep into each directory.
            "[linux] (F disc L | list partition tables)": Text("fdisk -l") + Key("enter"),                      # List partition tables and exit.
            "[linux] (I F config | interface config)":    Text("ifconfig") + Key("enter"),                      # Displays the configuration of all interfaces, both active and inactive. Close equivalent of Windows ipconfig. See https://askubuntu.com/questions/138119/ipconfig-not-working.
            "[linux] (I W config | network config)":      Text("iwconfig") + Key("enter"),                      # Display and change the parameters of the network interface which are specific to the wireless operation.
            "[linux] I P address ethernet":               Text("ip addr | grep \'inet .* eth0\'") + Key("enter"), # To find your system's internet IP address.
            "[linux] I P address wi-fi":                  Text("ip addr | grep \'inet .* wlan0\'") + Key("enter"), # To find your  system's Wi-Fi adapter IP address.
            "[linux] (List USB devices | L S USB)":       Text("lsusb") + Key("enter"),                         # Display information about USB buses in the system and the devices connected to them.
            "[linux] open cron tab":                      Text("sudo crontab -e") + Key("enter"),               # Open crontab for editing.
            "[linux] [(search | list)] wireless networks": Text("sudo iwlist scan | grep ESSID") + Key("enter"), # Searches and displays wireless networks.
            "[linux] (open sudoers file | edit steering file)": Text("sudo visudo") + Key("enter"),             # Steering file that governs which users and groups have access to the sudo command and even the capability to limit which programs they can execute via sudo.
            "[linux] [system] (halt | shutdown)":         Text("sudo halt") + Key("enter"),                     # Shutdown system.
            "[linux] [system] (reboot | restart)":        Text("sudo reboot") + Key("enter"),                   # Restart system.
            "linux version":                              Text("uname -a") + Key("enter"),                      # To check kernel and firmware versions.
            # Processes
            "[linux] kill process":                       Text("kill "),                                        # Kill a process.
            "[linux] (P S | display processes)":          Text("ps") + Key("enter"),                            # List current processes.
            "[linux] (P S F | display processes by user)": Text("ps -f") + Key("enter"),                         # List current processes and user spawned (UID).
            "[linux] (P S E F | display all processes)":  Text("ps -ef") + Key("enter"),                        # To see all information about all processes currently running on your system.
            "[linux] (P S aux | display processes plus)": Text("ps aux") + Key("enter"),                        # ps = report a snapshot of the current processes; a = show processes for all users; u = display the process's user/owner; x = also show processes not attached to a terminal.
            "linux (top | [(show | list)] running processes)": Text("top") + Key("enter"),                      # Tells you what's happening on system. Produces an ordered list of running processes selected by user-specified criteria, and updates it periodically.
        # dmesg - display messages from the kernel ring buffer
            "[linux] (D | driver) message more":          Text("dmesg | more") + Key("enter"),                  # List all loaded Drivers in Kernel,, display logs in a single page using more.
            "[linux] (D | driver) message less":          Text("dmesg | less") + Key("enter"),                  # List all loaded Drivers in Kernel,, display logs in a single page using less.
            "[linux] (D | driver) message head 20":       Text("dmesg | head -20") + Key("enter"),              # Print only the 1st 20 lines of output.
            "[linux] (D | driver) message tail 20":       Text("dmesg | tail -20") + Key("enter"),              # Print only the last 20 lines of output.
            "[linux] (D | driver) message grep":          Text("dmesg | grep -i "),                             # The -i option instructs grep command to ignore the case (upper or lower case letters).
            "[linux] (D | driver) message (grep S D A | devices)": Text("dmesg | grep sda"),                    # List all detected devices. Discover which hard disks have been detected by kernel.
        # Packages
            "[linux] list [installed] packages":          Text("dpkg --list") + Key("enter"),                   # List all installed packages.
            "[linux] list specific package":              Text("dpkg --list | "),                               # dpkg --list | <package_name>                                | List a specific package.
            "[linux] sudo apt get install":               Text("sudo apt-get install "),                        # sudo apt-get install <name>                                 | Install package.
            "[linux] sudo apt install":                   Text("sudo apt install "),                            # sudo apt install <name>                                     | Install package.
            "[linux] sudo apt get remove":                Text("sudo apt-get remove "),                         # sudo apt-get remove <name>                                  | Uninstall/delete/remove package.
            "[linux] sudo apt remove":                    Text("sudo apt remove "),                             # sudo apt remove <name>                                      | Uninstall/delete/remove package.
            "[linux] sudo apt get remove and purge":      Text("sudo apt-get --purge remove "),                 # sudo apt-get --purge remove <name>                          | Uninstall/delete/remove package along with all its configuration files.
            # Update                                                                                            # http://askubuntu.com/questions/196768/how-to-install-updates-via-command-line
            "[linux] sudo apt get update":                Text("sudo apt-get update") + Key("enter"),           # Updates the package lists for upgrades for packages that need upgrading, as well as new packages that have just come to the repositories.
            "[linux] sudo apt get upgrade":               Text("sudo apt-get upgrade") + Key("enter"),          # Strictly upgrades the current packages. Will fetch new versions of packages existing on the machine if APT knows about these new versions by way of apt-get update.
            "[linux] apt upgrade":                        Text("apt upgrade") + Key("enter"),                   # Strictly upgrades the current packages. Will fetch new versions of packages existing on the machine if APT knows about these new versions by way of apt-get update.
            "[linux] sudo apt get distribution upgrade":  Text("sudo apt-get dist-upgrade") + Key("enter"),     # Will do the same job which is done by apt-get upgrade, plus it will also intelligently handle the dependencies, so it might remove obsolete packages or add new ones. 
            # Cleanup
            "[linux] sudo apt get clean":                 Text("sudo apt-get clean") + Key("enter"),            # Clean the apt cache.
            "[linux] sudo apt get auto clean":            Text("sudo apt-get autoclean") + Key("enter"),        # Cleanup partial packages.
            "[linux] sudo apt get auto remove":           Text("sudo apt-get autoremove") + Key("enter"),       # Cleanup unused dependencies                                 | Removes packages that were installed by other packages and are no longer needed.
            # apt-file - allows you to search for specific file/package
            "[linux] install apt file":                   Text("sudo apt-get install apt-file") + Key("enter"), # Install.
            "[linux] apt file update":                    Text("sudo apt-file update") + Key("enter"),          # Update apt-file packages and dependencies database.
            "[linux] apt file search":                    Text("apt-file -l search "),                          # Search for package not yet installed with specific file.
            "[linux] apt file list":                      Text("apt-file list "),                               # List contents of a package not yet installed.
            "[linux] apt file upgradable":                Text("apt list --upgradable") + Key("enter"),         # List packages that can be upgraded.
        # List files                                                                                            List files and directories in...
            "[linux] (L S | list files)":                 Text("ls") + Key("enter"),                            # bare format.
            "[linux] L S (alpha | hidden)":               Text("ls -a") + Key("enter"),                         # bare format, include hidden files.
            "[linux] L S (P | [trailing] slash)":         Text("ls -p") + Key("enter"),                         # bare format with "/" character at the end of each directory.
            "[linux] L S F":                              Text("ls -F") + Key("enter"),                         # bare format with "/" character at the end of each directory.
            "[linux] L S head":                           Text("ls | head") + Key("enter"),                     # Only show the first 10 entries.
            "[linux] show tree":                          Text("tree") + Key("enter"),                          # Display a directory, all the sub-directories and files indented as a file structure.
            # One File Per Line
            "[linux] L S (1 | one per line)":             Text("ls -1") + Key("enter"),                         # bare format, one file per line.
            "[linux] L S (1 P | 1 [trailing] slash)":     Text("ls -1p") + Key("enter"),                        # bare format, one file per line with "/" character at the end of each directory.
            "[linux] L S 1 F":                            Text("ls -1F") + Key("enter"),                        # bare format, one file per line with "/" character at the end of each directory.
            # Long Form
            "[linux] (L S L | L S long form)":            Text("ls -l") + Key("enter"),
            "[linux] (L S L A | L S L hidden | list all files)": Text("ls -la") + Key("enter"),                 # long form, include hidden files.
            "[linux] L S L (P | [trailing] slash)":       Text("ls -lp") + Key("enter"),                        # long form with "/" character at the end of each directory.
            "[linux] L S L (H | human readable)":         Text("ls -lh") + Key("enter"),                        # long form with size in human readable format.
            "[linux] L S L (S | size)":                   Text("ls -lS") + Key("enter"),                        # long form, sort by file size; largest file first.
            "[linux] L S L (T | time)":                   Text("ls -lt") + Key("enter"),                        # long form, sort by last modified time.
            "[linux] L S L (T R | reverse time)":         Text("ls -ltr") + Key("enter"),                       # long form, sort by last modified time; reverse order.
            # Other
            "[linux] L S (R | recursive | subdirectories)": Text("ls -R") + Key("enter"),                       # Recursively list subdirectories.
        # FIND - Search File Names --> $ find [directory] [option] [file/folder]
            "[linux] find file windows":                  Text("find $HOME -name ''") + Key("left"),            # find $HOME -name '<name>'                                   | Find the home directory and all of its subdirectories.
            # Commands
            "linux find":                                 Text("find "),                                        # find <directory>                                            | Find command.
            "[linux] find files by name":                 Text("find  -type f -name ") + Key("left:15"),        # find <directory> -type f -name <name>                       | Find file by name.
            "[linux] find directory by name":             Text("find / -type d -name ") + Key("left"),          # find / -type d -name <name>                                 | Find directory by name.
            "[linux] find empty files by type":           Text("find  -type f -empty ") + Key("left:16"),       # find <directory> -type f -empty                             | Find empty files in a directory by type.
            "[linux] find executable files":              Text("find  -executable ") + Key("left:13"),          # find <directory> -executable <name>                         | Find by permissions: executable.
            "[linux] find writable files":                Text("find  -writable ") + Key("left:11"),            # find <directory> -writable <name>                           | Find by permissions: writable, i.e. not just read-only.
            # Flags
            "[linux] name flag":                          Text(" -name"),                                       # -name <name>                                                | Name flag.
            "[linux] type flag":                          Text(" -type"),                                       # -type <type>                                                | Type flag.
            "[linux] file type flag":                     Text(" -type f"),                                     # -type <type>                                                | Type flag.
            "[linux] directory type flag":                Text(" -type d"),                                     # -type <type>                                                | Type flag.
            "[linux] empty flag":                         Text(" -empty"),                                      # -empty                                                      | Empty flag.
            "[linux] executable flag":                    Text(" -executable"),                                 # -executable                                                 | executable flag.
            "[linux] writable flag":                      Text(" -writable"),                                   # -writable                                                   | writable flag.
        # GREP - Search File Contents --> $ grep [options] '[search_expression]' [directory]
            "[linux] history (search | grep)":            Text("history | grep "),                              # Find all the history commands that involve a certain string.
            "[linux] L S grep":                           Text("ls  | grep -Ei ") + Key("home, right:3"),       # ls <something> | grep -Ei <file>                            | Return with color and case insensitive flags.
            "[linux] list [installed] packages search":   Text("dpkg --list | grep -i ''") + Key("enter"),      # dpkg --list | grep -i '<query>'                             | List all queried installed packages.
            "[linux] ps aux grep":                        Text("ps aux | grep "),                               # Grep processes running on your computer.
            "[linux] (Z grep | search gzip)":             Text("zgrep "),                                       # zgrep <file>                                                | Search inside gzip files.
        # AWK - Will parse each field in the line (grep returns the entire line).
            "[linux] awk":                                Text("awk \'{ print  }\' "),                          # awk '{ print <column> }' <file_name>
            "[linux] awk (F | change delimiter)":         Text("awk -F \'{ print  }\' "),                       # awk -F<delimiter> '{ print <column> }' <file_name>
            "[linux] awk first column":                   Text("awk \'{ print $1 }\' "),                        # awk '{ print $1 }' <file_name>                              | Return 1st column.
            "[linux] awk regular expression":             Text("awk \'// { print }\' "),                        # awk '/<regex>/ { print }' <file_name>                       | Return regular expression.
            "[linux] awk if":                             Text("awk \'{ if($1 ~ //) print }\' "),               # awk '{ if($1 ~ /<regex>/)print }' <file_name>               | If statement on 1st column using regular expression.
        # File
            "[linux] copy file":                          Text("cp "),                                          # cp <source> <target>                                        | Copy file.
            "[linux] diff":                               Text("diff") + Key("enter"),                          # diff <file_1> <file_2>                                      | Diff files 1 and 2.
            "[linux] (move file | rename)":               Text("mv "),                                          # mv <source> <target>                                        | Move file (rename).
            "[linux] (remove | delete) file":             Text("rm "),                                          # rm <file>                                                   | Remove file.
            "[linux] (remove | delete) file F":           Text("rm -f "),                                       # rm <file> -f                                                | Force remove file.
            "[linux] (touch | (create | new) file)":      Text("touch "),                                       # touch <file_name>                                           | Create an empty file.
            "[linux] head <n>":                           Text("head  -n -%(n)d") + Key("home, right:5"),       # Show first <n> lines of file.
            "[linux] tail <n>":                           Text("tail  -n -%(n)d") + Key("home, right:5"),       # Show last <n> lines of file.
        # Directory
            "[linux] (make | create | new) (directory | folder)": Text("mkdir "),                               # mkdir <dirname>                                             | Make directory.
            "[linux] (make | create | new) (directory | folder) P": Text("mkdir -p "),                          # mkdir -p <dirname>                                          | Make directory. The -p flag will create nested directories, but only if they don't exist already.
            "[linux] (P W D | print working directory)":  Text("pwd") + Key("enter"),                           # Print working directory.
            "[linux] remove (directory | empty directory)": Text("rmdir "),                                     # rmdir <directory>                                           | Remove empty directory.
            "[linux] remove (directory recursively | non-empty directory)": Text("rm -rf "),                    # rm -rf <directory>                                          | Remove nonempty directory.
        # Change Directory
            "[linux] (C D | change directory)":           Text("cd "),                                          # Change directory.
            "[linux] C D dot dot":                        Text("cd ..") + Key("enter"),                         # Change directory one directory up.
            "[linux] (C D dot dot slash | (C D | up) one directory)": Text("cd ../") + Key("enter"),            # cd ../
            "[linux] (C D dot dot [slash] 2 | (C D | up) two directories)": Text("cd ../../") + Key("enter"),   # cd ../../
            "[linux] (C D (home | root) | home directory)": Text("cd ~") + Key("enter"),                        # Go to root directory.
            "[linux] C D (tilde | squiggly line)":        Text("cd ~/"),                                        # Change directory from root.
            "[linux] C D to path":                        Text("cd ~//") + Key("left"),                         # cd ~/<dirname>/                                             | Change directory to path include home directory.
        # SSH
            "[linux] (SSH I | connect to host)":          Text("ssh @") + Key("left"),                          # ssh <user>@<hostname>                                       | Connect and log into specified hostname.
            "[linux] (SSH I | connect to host with key)": Text("ssh -i  @") + Key("left:2"),                    # ssh -i <private_key_name> <user>@<hostname>                 | Connect and log into specified hostname using private key.
            "[linux] (SSH I with public key | connect to host with public key)": Text("ssh -i id_rsa @") + Key("left"), # ssh -i id_rsa <user>@<hostname>                     | Connect and log into specified hostname using id_rsa private key.
            "[linux] (SSH I root | connect to host as root)": Text("ssh -i  root@") + Key("left:6"),            # ssh -i <private_key_name> root@<hostname>                   | Connect and log into specified hostname as root using a private key.
            "[linux] open SSHD config file":              Text("sudo vi /etc/ssh/sshd_config") + Key("enter"),  # To disable root login --> PermitRootLogin, PermitEmptyPasswords, PasswordAuthentication should be set to no.
            "[linux] restart (SSHD service | daemon)":    Text("sudo service sshd restart") + Key("enter"),     # Restart daemon to pick up new config.
            # Specific Machines
            "[linux] (SSH I digital ocean | connect to digital ocean)": Text("ssh -i id_rsa @104.131.105.91") + Key("left:15"), # ssh -i id_rsa <user>@104.131.105.91         | Connect and log into DigitalOcean using id_rsa private key.
            "[linux] (SSH I raspberry pi | connect to raspberry pi)": Text("ssh -i id_rsa pi@192.168.0.55") + Key("enter"), # ssh -i id_rsa pi@192.168.0.55                   | Connect and log into Raspberry Pi using id_rsa private key.
            # Keys
            "[linux] copy public key to notepad":         Text("notepad < ~/.ssh/id_rsa.pub") + Key("enter"),   # Copies public key to Notepad.
            "[linux] (create | generate) [(SSH | public)] key": Text("ssh-keygen -t rsa -C \"\"") + Key("left"), # ssh-keygen -t rsa -C "<email>"                             | Create a new SSH key.
            "[linux] list public keys":                   Text("ls ~/.ssh/*.pub") + Key("enter"),               # List all public keys you have.
            "[linux] show public key":                    Text("cat ~/.ssh/id_rsa.pub") + Key("enter"),         # Show public key id_rsa.pub.
        # Secure Copy
            "[linux] secure copy local to remote":        Text("scp  @:/") + Key("left:4"),                     # scp <file> <your_username>@<remotehost>:/some/remote/directory                                                           | Copy the file "<file>" from the local host to a remote host
            "[linux] secure copy local to remote home":   Text("scp  @:~") + Key("left:4"),                     # scp <file1 file2> <your_username>@<remotehost>:~                                                                         | Copy the files "<file1>" and "<file2>" from the local host to your home directory on the remote host
            "[linux] secure copy remote to local":        Text("scp @: /") + Key("left:4"),                     # scp <your_username>@<remotehost>:<file> /some/local/directory                                                            | Copy the file "<file>" from a remote host to the local host
            "[linux] secure copy remote to remote":       Text("scp @:/ \@:/") + Key("left:8"),                 # scp <your_username>@<remotehost_1>:/some/remote/directory/<file> \<your_username>@<remotehost_2>:/some/remote/directory/ | Copy the file "<file>" from remote host "<remotehost_1>" to remote host "<remotehost_2>"
            "[linux] secure copy local port to remote":   Text("scp -P   @:/") + Key("left:5"),                 # scp -P <number> <file> <your_username>@<remotehost>:/some/remote/directory                                               | Copy the file "<file>" from the local host to a remote host using port <number>
            "[linux] secure copy local directory to remote": Text("scp -r  @:/") + Key("left:4"),               # scp -r <local_directory> <your_username>@<remotehost>:/some/remote/directory/<remote_directory>                          | Copy the directory "<local_directory>" from the local host to a remote host's directory "<remote_directory>"
            "[linux] secure copy remote to local current directory": Text("scp @:/\{\} .") + Key("left:9"),     # scp <your_username>@<remotehost>:/some/remote/directory/\{<file1,file2,file3>\} .                                        | Copy multiple files from the remote host to your current directory on the local host
        # Curl
            "[linux] curl (big I | head request)":        Text("curl -I "),                                     # Sends a HEAD request. Only response headers are printed.
            "[linux] curl (I | show response header)":    Text("curl -i "),                                     # Prints response headers along with response content.
            "[linux] curl gzip test":                     Text("curl -i -H \"Accept-Encoding: gzip,deflate\" http://") + Key("enter"), # cURL testing gzip response.
            "[linux] curl local host":                    Text("curl -i 127.0.0.1:3000/") + Key("enter"),       # curl -i 127.0.0.1:3000/
            "[linux] curl Public IP":                     Text("curl -4 icanhazip.com") + Key("enter"),         # Should give you your public IP addresses as seen from another location on the Internet.
        # Logs and Tail
            "linux tail":                                 Text("sudo tail "),                                   # sudo tail <file_name>                                       | Output the last part of files.
            "[linux] (view | show) logs":                 Text("sudo cat /var/log/auth.log") + Key("enter"),    # View log files.
            "[linux] tail F":                             Text("sudo tail -f "),                                # sudo tail -ff <file_name>                                   | Output the last part of files, -f flag (follow) outputs appended data as the file grows.
            # apt-get install fail2ban
            "[linux] tail log":                           Text("sudo tail /var/log/fail2ban.log") + Key("enter"), # sudo tail /var/log/fail2ban.log                           | Last few things happening on your server.
            "[linux] tail log [and] follow":              Text("sudo tail -f /var/log/fail2ban.log") + Key("enter"), # sudo tail -f /var/log/fail2ban.log                     | Real-time stream of what's happening on your server.
        # Shells
            "[linux] cat shells":                         Text("cat /etc/shells") + Key("enter"),               # cat /etc/shells                                             | List acceptable shells to change to.
            "[linux] change shell to bash":               Text("chsh -s /bin/bash") + Key("enter"),             # chsh -s /bin/bash                                           | Change shell to bash.
            "[linux] change shell to S H":                Text("chsh -s /bin/sh") + Key("enter"),               # chsh -s /bin/sh                                             | Change shell to sh.
            "[linux] edit z shell profile":               Text("gedit ~/.zsh_profile") + Key("enter"),          # gedit ~/.zsh_profile
            "[linux] edit z shell":                       Text("gedit ~/.zsh|c") + Key("enter"),                # gedit ~/.zsh|c
            "[linux] sudo bash":                          Text("sudo bash") + Key("enter"),                     # This command runs "bash" as a super user.
            "[linux] (what shell [am i using] | echo 0)": Text("echo $0") + Key("enter"),                       # To see what shell you are using.
        # Nginx
            "[linux] engine X":                           Text("nginx "),                                       # nginx
            "[linux] engine X (T | test)":                Text("sudo nginx -t") + Key("enter"),                 # Runs configuration file, does quick validation to ensure working properly.
            "[linux] engine X reload":                    Text("sudo service nginx reload") + Key("enter"),     # Reload.
            "[linux] engine X restart":                   Text("sudo service nginx restart") + Key("enter"),    # Restart.
        # UFW - Uncomplicated Firewall
            "[linux] UFW allow":                          Text("sudo ufw allow "),                              # sudo ufw allow <type>                                       | Allow connections.
            "[linux] UFW delete <n>":                     Text("sudo ufw delete %(n)d") + Key("enter"),         # sudo ufw delete <n>                                         | Delete rule by status number --> sudo ufw status numbered
            "[linux] UFW disable":                        Text("sudo ufw disable") + Key("enter"),              # To disable UFW.
            "[linux] UFW enable":                         Text("sudo ufw enable") + Key("enter"),               # To enable UFW.
            "[linux] UFW reset":                          Text("sudo ufw reset"),                               # Reset your cloud server's rules to the default settings.
            "[linux] UFW status":                         Text("sudo ufw status") + Key("enter"),               # Check the status of UFW.
            "[linux] UFW status numbered":                Text("sudo ufw status numbered") + Key("enter"),      # Check the status of UFW.
        # Redirection Operators
            "([linux] standard out | linux (pipe | pipes))": Text(" | "),                                       # Read from standard output. What are we outputting?
            "[linux] write to file":                      Text(" > "),                                          # Write standard output to file. Just point to the file you want to write to.
            "[linux] append to file":                     Text(" >> "),                                         # Append standard output to file.
            "[linux] read from file":                     Text(" < "),                                          # Read from standard in. What are we reading from a file?
            "[linux] standard error":                     Text(" 2> "),                                         # Read from standard error. If there's an error, here's what were doing with it.
        # Change Mode
            "[linux] (C H | change) (mod | mode) to 777":         Text("sudo chmod 777 "),                      # sudo chmod 777 <file>         | rwx rwx rwx | Anybody can read, write, execute.                                          | 0 No Permission
            "[linux] (C H | change) (mod | mode) to 775":         Text("sudo chmod 775 "),                      # sudo chmod 775 <file>         | rwx rwx r-x | Owner and Group can read, write, execute. Everyone else can read, execute. | 1 Execute
            "[linux] (C H | change) (mod | mode) to 774":         Text("sudo chmod 774 "),                      # sudo chmod 774 <file>         | rwx rwx r-- | Owner and Group can read, write, execute.  Everyone else can read.         | 2 Write
            "[linux] (C H | change) (mod | mode) to 755":         Text("sudo chmod 755 "),                      # sudo chmod 755 <file>         | rwx r-x r-x | Owner can read, write, execute. Everyone else can read, execute.           | 3 Write, Execute
            "[linux] (C H | change) (mod | mode) to 700":         Text("sudo chmod 700 "),                      # sudo chmod 700 <file>         | rwx --- --- | Owner can read, write, execute. No one else has any rights.                | 4 Read
            "[linux] (C H | change) (mod | mode) to 666":         Text("sudo chmod 666 "),                      # sudo chmod 666 <file>         | rw- rw- rw- | Everyone can read, write.                                                  | 5 Read, Execute
            "[linux] (C H | change) (mod | mode) to 664":         Text("sudo chmod 664 "),                      # sudo chmod 664 <file>         | rw- rw- r-- | Owner and Group can read, write. Everyone else can read.                   | 6 Read, Write
            "[linux] (C H | change) (mod | mode) to 644":         Text("sudo chmod 644 "),                      # sudo chmod 644 <file>         | rw- r-- r-- | Owner can read, write. Everyone else can read.                             | 7 Read, Write, Execute
            "[linux] (C H | change) (mod | mode) to 777 recursively": Text("sudo chmod -R 777 "),               # sudo chmod -R 777 <directory> | rwx rwx rwx | Anybody can read, write, execute.                                          | 
            "[linux] (C H | change) (mod | mode) to 775 recursively": Text("sudo chmod -R 775 "),               # sudo chmod -R 775 <directory> | rwx rwx r-x | Owner and Group can read, write, execute. Everyone else can read, execute. | 
            "[linux] (C H | change) (mod | mode) to 774 recursively": Text("sudo chmod -R 774 "),               # sudo chmod -R 774 <directory> | rwx rwx r-- | Owner and Group can read, write, execute.  Everyone else can read.         | 
            "[linux] (C H | change) (mod | mode) to 755 recursively": Text("sudo chmod -R 755 "),               # sudo chmod -R 755 <directory> | rwx r-x r-x | Owner can read, write, execute. Everyone else can read, execute.           | 
            "[linux] (C H | change) (mod | mode) to 700 recursively": Text("sudo chmod -R 700 "),               # sudo chmod -R 700 <directory> | rwx --- --- | Owner can read, write, execute. No one else has any rights.                | 
            "[linux] (C H | change) (mod | mode) to 666 recursively": Text("sudo chmod -R 666 "),               # sudo chmod -R 666 <directory> | rw- rw- rw- | Everyone can read, write.                                                  | 
            "[linux] (C H | change) (mod | mode) to 664 recursively": Text("sudo chmod -R 664 "),               # sudo chmod -R 664 <directory> | rw- rw- r-- | Owner and Group can read, write. Everyone else can read.                   | 
            "[linux] (C H | change) (mod | mode) to 644 recursively": Text("sudo chmod -R 644 "),               # sudo chmod -R 644 <directory> | rw- r-- r-- | Owner can read, write. Everyone else can read.                             | 
        # Raspberry Pi
            "[raspberry] pi configure":                   Text("sudo raspi-config") + Key("enter"),             # Configuration program.
            "[raspberry] pi remote (server | viewing)":   Text("tightvncserver") + Key("enter"),                # Startup TightVNC server.
            "[raspberry] pi shutdown":                    Text("sudo shutdown -h now") + Key("enter"),          # To properly shut down Raspberry Pi.
            "[raspberry] pi update firmware":             Text("sudo rpi-update") + Key("enter"),               # Checks whether a new firmware version is available and downloads it if necessary.

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 0, 100)
           ],
    defaults = {
        "n": 1,
        }
    )

grammar.add_rule(linux_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

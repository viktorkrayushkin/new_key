Last login: Mon Mar 14 23:55:28 on console
viktor@MBP-Viktor ~ % ssh-keygen -t ed25519 -C "gokertymgre68@gmail.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/viktor/.ssh/id_ed25519): new_key
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in new_key
Your public key has been saved in new_key.pub
The key fingerprint is:
SHA256:iTG0Y0HQooVVEJDKpDc8N078E9ZbQolQhZtmWwC3YTA gokertymgre68@gmail.com
The key's randomart image is:
+--[ED25519 256]--+
|  .=E%X+..       |
| .o o===o        |
|+o + .B*         |
|o.* =.B=+..      |
| . * *.+S+       |
|    . + .        |
|       .         |
|                 |
|                 |
+----[SHA256]-----+
viktor@MBP-Viktor ~ % open /Users/viktor/.ssh/id_ed25519
The file /Users/viktor/.ssh/id_ed25519 does not exist.
viktor@MBP-Viktor ~ % open /Users/viktor/.ssh/id_ed25519/ new_key
The file /Users/viktor/.ssh/id_ed25519 does not exist.
viktor@MBP-Viktor ~ % open /Users/viktor/.ssh/id_ed25519/new_key 
The file /Users/viktor/.ssh/id_ed25519/new_key does not exist.
viktor@MBP-Viktor ~ % cd .ssh
viktor@MBP-Viktor .ssh % cd id_ed25519
cd: no such file or directory: id_ed25519
viktor@MBP-Viktor .ssh % open new_key
The file /Users/viktor/.ssh/new_key does not exist.
viktor@MBP-Viktor .ssh % open /id_ed25519/ new_key
The files /id_ed25519 and /Users/viktor/.ssh/new_key do not exist.
viktor@MBP-Viktor .ssh % open new_key
The file /Users/viktor/.ssh/new_key does not exist.
viktor@MBP-Viktor .ssh % open /Users/viktor/new_key
viktor@MBP-Viktor .ssh % shh-add /Users/viktor/new_key
zsh: command not found: shh-add
viktor@MBP-Viktor .ssh % cd viktor
cd: no such file or directory: viktor
viktor@MBP-Viktor .ssh % cd /Users/viktor
viktor@MBP-Viktor ~ % shh-add /Users/viktor/new_key
zsh: command not found: shh-add
viktor@MBP-Viktor ~ % shh-add .shh/new_key
zsh: command not found: shh-add
viktor@MBP-Viktor ~ % cd shh
cd: no such file or directory: shh
viktor@MBP-Viktor ~ % cd .shh
cd: no such file or directory: .shh
viktor@MBP-Viktor ~ % /Users/viktor/.shh
zsh: no such file or directory: /Users/viktor/.shh
viktor@MBP-Viktor ~ % /Users/viktor/shh
zsh: no such file or directory: /Users/viktor/shh
viktor@MBP-Viktor ~ % cd /Users/viktor/.shh
cd: no such file or directory: /Users/viktor/.shh
viktor@MBP-Viktor ~ % cd /Users/viktor/shh
cd: no such file or directory: /Users/viktor/shh
viktor@MBP-Viktor ~ % cd shh
cd: no such file or directory: shh
viktor@MBP-Viktor ~ % cd /shh
cd: no such file or directory: /shh
viktor@MBP-Viktor ~ % cd .shh
cd: no such file or directory: .shh
viktor@MBP-Viktor ~ % cd .ssh
viktor@MBP-Viktor .ssh % ssh-add /Users/viktor/new_key
Identity added: /Users/viktor/new_key (gokertymgre68@gmail.com)
viktor@MBP-Viktor .ssh % ssh-add -l
256 SHA256:iTG0Y0HQooVVEJDKpDc8N078E9ZbQolQhZtmWwC3YTA gokertymgre68@gmail.com (ED25519)
viktor@MBP-Viktor .ssh % shh -T git@github.com
zsh: command not found: shh
viktor@MBP-Viktor .ssh % ssh -T git@github.com
Hi viktorkrayushkin! You've successfully authenticated, but GitHub does not provide shell access.
viktor@MBP-Viktor .ssh % git config --global user.name "viktorkrayushkin"
viktor@MBP-Viktor .ssh % git config --global user.email "gokertymgre68@gmail.com"
viktor@MBP-Viktor .ssh %  cd /Users/viktor 
viktor@MBP-Viktor ~ % cd repositor 
viktor@MBP-Viktor repositor % git clone git@github.com:viktorkrayushkin/new_key.git
Cloning into 'new_key'...
warning: You appear to have cloned an empty repository.
viktor@MBP-Viktor repositor % cd ney_key
cd: no such file or directory: ney_key
viktor@MBP-Viktor repositor % cd new_key
viktor@MBP-Viktor new_key % cd /Users/viktor/repositor/new_key 
viktor@MBP-Viktor new_key % cd /Users/viktor/repositor/new_key  
viktor@MBP-Viktor new_key % git log
fatal: your current branch 'master' does not have any commits yet
viktor@MBP-Viktor new_key % 

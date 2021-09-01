# IAC - Terraform

After a spent huge time I decided to write this .md file. I attach all files that I used but I was not able to set up the system due to the problem that I have MacOS - Big Sur, and a always faced an error after attempting to set up VM.
```shell
virtualbox_vm.node[0]: Still creating... [1m20s elapsed]
virtualbox_vm.node[0]: Still creating... [1m30s elapsed]
╷
│ Error: [ERROR] Setup VM properties: exit status 1
│ 
│   with virtualbox_vm.node[0],
│   on main.tf line 13, in resource "virtualbox_vm" "node":
│   13: resource "virtualbox_vm" "node" {
│ 
╵
╷
│ Error: [ERROR] Setup VM properties: exit status 1
│ 
│   with virtualbox_vm.node[1],
│   on main.tf line 13, in resource "virtualbox_vm" "node":
│   13: resource "virtualbox_vm" "node" {
```

So, near I put a solution with aws image creating
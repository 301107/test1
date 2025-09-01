from plumbum import local

# Выполнение shell-команды
ls = local['ls']
print(ls('-l'))

# Комбинирование команд как в shell
print((local['ls']['-la'] | local['grep']['py'])())

# Работа с файлами
from plumbum.cmd import cp, rm
cp('a.txt', 'b.txt')
rm('-f', 'b.txt')

# Удалённое выполнение по SSH
from plumbum.machines import SshMachine
with SshMachine('remote.host.com', user='user') as remote:
    print(remote['uname']('-a'))
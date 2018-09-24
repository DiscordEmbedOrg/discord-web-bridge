# Prologue

Systemd is a nice tool to start, stop, restart scripts on your linux machine. If your script crashes or the VPS does a system reboot your scripts will come back online.  
In order to use this you need to be on Linux, have systemd, the discord-web-bridge bot has been properly installed and it has worked before.

# Setup

Get python path:
```
root@TinVultr:~# which python3
/usr/bin/python3
root@TinVultr:~# which python3.5
/usr/bin/python3.5
```

Get crossbar path:
```
root@TinVultr:~# which crossbar
/usr/local/bin/crossbar
```

```
cd /etc/systemd/system
nano crossbar.service
nano discord-web-bridge.service
```

You can see my .service files. They will not work for you and you have to adjust the paths accordingly.
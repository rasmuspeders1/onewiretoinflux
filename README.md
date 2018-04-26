# onewiretoinflux

Use ansible to install. goto the ansible subdirectory of this repo and run the playbook against your raspberry pi.
Requires owhttpd daemon and influxdb to be installed and running.

owhttpd is installed automatically by the ansible playbook. you need to install influxdb yourself with your preferred method.

`cd ansible`

`ansible-playbook play.yml -i "192.168.1.5," -u pi --ask-become-pass`

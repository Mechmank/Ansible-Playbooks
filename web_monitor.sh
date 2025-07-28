#!/bin/bash
# check if httpd or nginx is installed
if 
    systemctl list-units --type=service --all | grep -q httpd; 
    then 
    service="httpd"
elif 
    systemctl list-units --type=service --all | grep -q nginx; 
    then 
    service="nginx"
else
    echo "$(date) : NO web service found" >> /var/log/web_service_monitor.log
exit 1
fi

# Check if running
if ! systemctl is-active --quiet $service; then
    systemctl start  $service
    echo "$(date) : $service was down and restarted" >> /var/log/web_service_monitor.log
else
    echo "$(date) : $service is running fine" >> /var/log/web_service_monitor.log
fi
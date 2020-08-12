## Description
This tool is created with the intension of tracking YouTube.com data usage by the system apps. It uses network monitoring tool called iftop. Iftop is capable of filtering data packets using pcap filtering expressions. So that I used network mask of youtube.com and my ISPs cache server to filter incoming and outgoing data packets. Most of the ISPs use caching server to deliver YouTube videos much faster. You can find IP address of that server by inspecting youtube.com website through a browser. Then I used whois tool to find CIDR of that host. You can use dig or nslookup tools to find ip address of YouTube. As it is hard to separate YouTube ip addresses using network mask from other Google services, this may not cover whole ip addresses belong to the YouTube. But most of the time YouTube videos are delivered through caching server of the ISP. So that, it won't be a huge problem.
## Required tools

* iftop

  ```
  sudo apt install iftop
  ```

## How to use

1. First you have to change report saving path in the track.sh

2. Change ExecStart path in data-track.service point to track.sh

3. Create symbolic link for data-track.service

	```
	sudo ln -s data-track.service /etc/systemd/system/data-track.service
	```

4. Reload systemctl

   ```
   sudo systemctl daemon-reload
   ```

5. Enable the service to run on system startup

   ```
   sudo systemctl enable data-track.service
   ```

6. Start the service

   ```
   sudo systemctl start data-track.service
   ```

7. Check whether service is started properly

   ```
   sudo systemctl status data-track.service
   ```

8. Calculate total data usage (data-track.service logs report in every 5 minutes. You can change this duration in track.sh)

   ```
   python3 report.py
   ```

   
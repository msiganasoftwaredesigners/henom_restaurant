[0;1;32m●[0m gunicorn.service - gunicorn daemon
     Loaded: loaded (]8;;file://srv580216/etc/systemd/system/gunicorn.service/etc/systemd/system/gunicorn.service]8;;; [0;1;38;5;185mdisabled[0m; preset: [0;1;32menabled[0m)
     Active: [0;1;32mactive (running)[0m since Fri 2025-11-21 08:15:50 UTC; 13s ago
TriggeredBy: [0;1;32m●[0m gunicorn.socket
   Main PID: 4021 (gunicorn)
      Tasks: 4 (limit: 4654)
     Memory: 124.8M (peak: 124.9M)
        CPU: 935ms
     CGroup: /system.slice/gunicorn.service
             ├─[0;38;5;245m4021 /var/www/henom_restaurant/venv/bin/python3 /var/www/henom_restaurant/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock msigana_ecommerce.wsgi:application[0m
             ├─[0;38;5;245m4054 /var/www/henom_restaurant/venv/bin/python3 /var/www/henom_restaurant/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock msigana_ecommerce.wsgi:application[0m
             ├─[0;38;5;245m4055 /var/www/henom_restaurant/venv/bin/python3 /var/www/henom_restaurant/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock msigana_ecommerce.wsgi:application[0m
             └─[0;38;5;245m4056 /var/www/henom_restaurant/venv/bin/python3 /var/www/henom_restaurant/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock msigana_ecommerce.wsgi:application[0m

Nov 21 08:15:50 srv580216 systemd[1]: Started gunicorn.service - gunicorn daemon.
Nov 21 08:15:50 srv580216 gunicorn[4021]: [2025-11-21 08:15:50 +0000] [4021] [INFO] Starting gunicorn 20.1.0
Nov 21 08:15:50 srv580216 gunicorn[4021]: [2025-11-21 08:15:50 +0000] [4021] [INFO] Listening at: unix:/run/gunicorn.sock (4021)
Nov 21 08:15:50 srv580216 gunicorn[4021]: [2025-11-21 08:15:50 +0000] [4021] [INFO] Using worker: sync
Nov 21 08:15:50 srv580216 gunicorn[4054]: [2025-11-21 08:15:50 +0000] [4054] [INFO] Booting worker with pid: 4054
Nov 21 08:15:51 srv580216 gunicorn[4055]: [2025-11-21 08:15:51 +0000] [4055] [INFO] Booting worker with pid: 4055
Nov 21 08:15:51 srv580216 gunicorn[4056]: [2025-11-21 08:15:51 +0000] [4056] [INFO] Booting worker with pid: 4056

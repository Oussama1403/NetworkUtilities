# Description

PHP 5.4 and later have a [built-in web server](http://www.php.net/manual/en/features.commandline.webserver.php).
It is very helpful to quickly test a php app without the need to install other Web Servers.

## Usage
From your terminal:
```bash
cd /../../dir
```
and then type:
```bash
php -S 127.0.0.1:8000 phpfile.php
```
or if you want to specify the directory root
```bash
php -S 127.0.0.1:8000 -t your_folder/
```
(The name of the PHP file inside the root folder must be index.php)


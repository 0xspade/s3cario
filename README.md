# s3cario
[![Python |3.8](https://img.shields.io/badge/python-3.8-yellow.svg)](https://www.python.org/) [![Twitter](https://img.shields.io/badge/twitter-@0xspade-blue.svg)](https://twitter.com/0xspade)

This tool is based in [S3Cruze](https://github.com/JR0ch17/S3Cruze) tool of [@JR0ch17](https://twitter.com/JR0ch17). Translated from python2 to python3, remove the feature of bruteforce. The other feature still remains and upgraded. You can check a single domain or a subdomain list from your recon results. This tool will get the CNAME first if it's a valid Amazon s3 bucket and if it's not, it will try to check if the domain is a bucket name. You can also try both in single domain option (but not available with subdomain list option).

[![asciicast](https://asciinema.org/a/mfgqR7fNPok2ovY1h5x0cQdvz.svg)](https://asciinema.org/a/mfgqR7fNPok2ovY1h5x0cQdvz)

## Installation

```shell
$ git clone https://github.com/0xspade/s3cario.git
$ cd s3cario
$ pip3 install -r requirements.txt
```
OR

```shell
$ git clone https://github.com/0xspade/s3cario.git
$ cd s3cario
$ python3 -m pip install -r requirements.txt
```

**AWS-CLI**

```shell
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]:
Default output format [None]:
```

## Usage

**Single domain/subdomain**
```shell
python3 s3cario.py -d test.example.com -t -u -r --all
```

**Subdomain list**
```shell
python3 s3cario.py -dL subdomain_list.txt -s -u -r --all
```

**pipe it from another tools**
```shell
subfinder -d example.com -nW -silent | python3 s3cario.py --pipe -t -u -r --all
```

## Help

```shell
$ python3 s3cario.py -h


		███████╗██████╗  ██████╗ █████╗ ██████╗ ██╗ ██████╗ 
		██╔════╝╚════██╗██╔════╝██╔══██╗██╔══██╗██║██╔═══██╗
		███████╗ █████╔╝██║     ███████║██████╔╝██║██║   ██║
		╚════██║ ╚═══██╗██║     ██╔══██║██╔══██╗██║██║   ██║
		███████║██████╔╝╚██████╗██║  ██║██║  ██║██║╚██████╔╝
		╚══════╝╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝ v0.2
		                                     		@0xspade
	
usage: s3cario.py [-h] [-d [DOMAIN]] [-dL [DOMAINLIST]] [--pipe] [-t] [-s] [-v] [-u] [-r] [-a] [-p] [-c] [-rP] [-w] [-l] [--all]

optional arguments:
  -h, --help            show this help message and exit
  -d [DOMAIN], --domain [DOMAIN]
                        Target Domain or Subdomain
  -dL [DOMAINLIST], --domainList [DOMAINLIST]
                        Target Domain/Subdomain list
  --pipe                Read domains in pipe
  -t, --test            Test the domain also
  -s, --silent          No Errors
  -v, --view            List files bucket
  -u, --upload          Upload to bucket
  -r, --remove          Delete file after upload
  -a, --acl             View ACL configuration
  -p, --policy          View bucket policy
  -c, --cors            View CORS configuration
  -rP, --replication    View replication configuration
  -w, --website         View website configuration
  -l, --location        View bucket location
  --all                 View ALL configuration
```

## Disclaimer

This tool is for bug bounty or gray box penetration testing only. Be responsible with your action using my tool. I'm not responsible for the others action who misuse my tool.

My code is look like a copy paste and a shitty "if and else" code. But as long as it's working, I guess it's a good to go tool :)

Feel free to translate it to golang.


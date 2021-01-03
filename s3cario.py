#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, subprocess, requests, argparse, os.path, os, re, colorama
from random import randrange
from colorama import Fore, Back, Style
colorama.init()

cmd = subprocess.getoutput

def banner():
	banner = """

		███████╗██████╗  ██████╗ █████╗ ██████╗ ██╗ ██████╗ 
		██╔════╝╚════██╗██╔════╝██╔══██╗██╔══██╗██║██╔═══██╗
		███████╗ █████╔╝██║     ███████║██████╔╝██║██║   ██║
		╚════██║ ╚═══██╗██║     ██╔══██║██╔══██╗██║██║   ██║
		███████║██████╔╝╚██████╗██║  ██║██║  ██║██║╚██████╔╝
		╚══════╝╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝ v0.1
		                                     		@0xspade
	"""
	print(Fore.CYAN+banner+Style.RESET_ALL)

def separator():
	print(Fore.WHITE+"*"*30+Style.RESET_ALL)

def upload(bucket, remove=False, domainList=False):
	random_number = randrange(10000000, 99999999)
	file = "poc-"+str(random_number)+"-"+bucket+".txt"
	new_file = file
	upload = open(new_file, 'w+')
	upload.write("Proof Of Concept\nAWS Misconfig\n-/Spade Was Here-/") ## Replace Me :)
	upload.close()

	if domainList is False: print(Fore.YELLOW+"[!] Trying Upload: "+file+Style.RESET_ALL)
	up = cmd("aws s3 cp %s s3://%s" % (new_file, bucket))
	if 'An error occurred (AccessDenied) when calling the PutObject operation: Access Denied' in up or '(AllAccessDisabled)' in up:
		print(Fore.RED+'\b\t[Upload Failed]'+Style.RESET_ALL) if domainList else print(Fore.RED+'[X] Access Denied for Uploading in bucket'+Style.RESET_ALL)
		if remove and domainList: 
			print(Fore.YELLOW+'\b\t[Remove DNF]'+Style.RESET_ALL)
		elif remove: 
			print(Fore.YELLOW+'[!] Remove will not continue'+Style.RESET_ALL)
	elif '(NoSuchBucket)' in up:
		print(Fore.MAGENTA+'\b\t[NSB:Upload Failed]'+Style.RESET_ALL) if domainList else print(Fore.MAGENTA+'[X] No Such Bucket for Uploading in bucket'+Style.RESET_ALL)
		if remove and domainList: 
			print(Fore.YELLOW+'\b\t[NSB:Remove DNF]'+Style.RESET_ALL)	
		elif remove: 
			print(Fore.YELLOW+'[!] Remove will not continue'+Style.RESET_ALL)	
	else:
		separator()
		print('\b\t[Upload Success]') if domainList else print(up+"\n")
		separator()	

		if remove:
			print(Fore.YELLOW+"[!] Trying Remove: "+new_file+Style.RESET_ALL)
			rm = cmd("aws s3 rm s3://%s/%s" %(bucket, new_file))
			separator()
			print('\b\t[Remove Success]') if domainList else print(rm+"\n")
			separator()
		os.remove(new_file)

def acl(bucket, domainList=False):
	if domainList is False: print(Fore.YELLOW+"[!] Checking "+bucket+" bucket ACL: "+Style.RESET_ALL)
	acl = cmd("aws s3api get-bucket-acl --bucket %s" %(bucket))
	if 'An error occurred (AccessDenied) when calling the GetBucketAcl operation: Access Denied' in acl or '(AllAccessDisabled)' in acl:
		print(Fore.RED+'\b\t[ACL Disable]'+Style.RESET_ALL) if domainList else print(Fore.RED+'[X] Access Denied for fetching bucket ACL'+Style.RESET_ALL)
	elif '(NoSuchBucket)' in acl:
		print(Fore.MAGENTA+'\b\t[NSB:ACL Disable]'+Style.RESET_ALL) if domainList else print(Fore.MAGENTA+'[X] No Such Bucket for fetching bucket ACL'+Style.RESET_ALL)
	else:
		separator()
		print('\b\t[ACL Enable]') if domainList else print(acl+"\n")
		separator()	

def policy(bucket, domainList=False):
	if domainList is False: print(Fore.YELLOW+"[!] Checking "+bucket+" bucket policy: "+Style.RESET_ALL)
	policy = cmd("aws s3api get-bucket-policy --bucket %s" %(bucket))
	if 'An error occurred (AccessDenied) when calling the GetBucketPolicy operation: Access Denied' in policy or '(AllAccessDisabled)' in policy:
		print(Fore.RED+'\b\t[Policy Disable]'+Style.RESET_ALL) if domainList else print(Fore.RED+'[X] Access Denied for fetching bucket policy'+Style.RESET_ALL)
	elif '(NoSuchBucket)' in policy:
		print(Fore.MAGENTA+'\b\t[NSB:Policy Disable]'+Style.RESET_ALL) if domainList else print(Fore.MAGENTA+'[X] No Such Bucket for fetching bucket policy'+Style.RESET_ALL)
	else:
		separator()
		print('\b\t[Policy Enable]') if domainList else print(policy+"\n")
		separator()	

def cors(bucket, domainList=False):
	if domainList is False: print(Fore.YELLOW+"[!] Checking "+bucket+" bucket CORS config: "+Style.RESET_ALL)
	cors = cmd("aws s3api get-bucket-cors --bucket %s" %(bucket))
	if 'An error occurred (AccessDenied) when calling the GetBucketCors operation: Access Denied' in cors or '(AllAccessDisabled)' in cors:
		print(Fore.RED+'\b\t[Cors Disable]'+Style.RESET_ALL) if domainList else print(Fore.RED+'[X] Access Denied for fetching cors config'+Style.RESET_ALL)
	elif '(NoSuchBucket)' in cors:
		print(Fore.MAGENTA+'\b\t[NSB:Cors Disable]'+Style.RESET_ALL) if domainList else print(Fore.MAGENTA+'[X] No Such Bucket for fetching cors config'+Style.RESET_ALL)
	else:
		separator()
		print('\b\t[Cors Enable]') if domainList else print(cors+"\n")
		separator()	

def replication(bucket, domainList=False):
	if domainList is False: print(Fore.YELLOW+"[!] Checking "+bucket+" bucket replication config: "+Style.RESET_ALL)
	replication = cmd("aws s3api get-bucket-replication --bucket %s" %(bucket))
	if 'An error occurred (AccessDenied) when calling the GetBucketReplication operation: Access Denied' in replication or '(AllAccessDisabled)' in replication:
		print(Fore.RED+'\b\t[Replication Disable]'+Style.RESET_ALL) if domainList else print(Fore.RED+'[X] Access Denied for fetching replication config'+Style.RESET_ALL)
	elif '(NoSuchBucket)' in replication:
		print(Fore.MAGENTA+'\b\t[NSB:Replication Disable]'+Style.RESET_ALL) if domainList else print(Fore.MAGENTA+'[X] No Such Bucket for fetching replication config'+Style.RESET_ALL)
	else:
		separator()
		print('\b\t[Replication Enable]') if domainList else print(replication+"\n")
		separator()	

def website(bucket, domainList=False):
	if domainList is False: print(Fore.YELLOW+"[!] Checking "+bucket+" bucket website config: "+Style.RESET_ALL)
	website = cmd("aws s3api get-bucket-website --bucket %s" %(bucket))
	if 'An error occurred (AccessDenied) when calling the GetBucketWebsite operation: Access Denied' in website or '(AllAccessDisabled)' in website:
		print(Fore.RED+'\b\t[Website Disable]'+Style.RESET_ALL) if domainList else print(Fore.RED+'[X] Access Denied for fetching website config'+Style.RESET_ALL)
	elif '(NoSuchBucket)' in website:
		print(Fore.MAGENTA+'\b\t[NSB:Website Disable]'+Style.RESET_ALL) if domainList else print(Fore.MAGENTA+'[X] No Such Bucket for fetching website config'+Style.RESET_ALL)
	else:
		separator()
		print('\b\t[Website Enable]') if domainList else print(website+"\n")
		separator()	

def location(bucket, domainList=False):
	if domainList is False: print(Fore.YELLOW+"[!] Checking "+bucket+" bucket location: "+Style.RESET_ALL)
	location = cmd("aws s3api get-bucket-location --bucket %s" %(bucket))
	if 'An error occurred (AccessDenied) when calling the GetBucketLocation operation: Access Denied' in location or '(AllAccessDisabled)' in location:
		print(Fore.RED+'\b\t[Location Disable]'+Style.RESET_ALL) if domainList else print(Fore.RED+'[X] Access Denied for fetching bucket location'+Style.RESET_ALL)
	elif '(NoSuchBucket)' in location:
		print(Fore.MAGENTA+'\b\t[NSB:Location Disable]'+Style.RESET_ALL) if domainList else print(Fore.MAGENTA+'[X] No Such Bucket for fetching bucket location'+Style.RESET_ALL)
	else:
		separator()
		print('\b\t[Location Enable]') if domainList else print(location+"\n")
		separator()	

def listbucket(bucket, domainList=False):
	if domainList is False: print(Fore.YELLOW+"[!] Trying to list files in "+bucket+Style.RESET_ALL )
	listbucket = cmd("aws s3 ls s3://%s" %(bucket))
	if 'An error occurred (AccessDenied) when calling the ListObjectsV2 operation: Access Denied' in listbucket or '(AllAccessDisabled)' in listbucket:
		print(Fore.RED+'\b\t[List Disable]'+Style.RESET_ALL) if domainList else print(Fore.RED+'[X] Access Denied for List files'+Style.RESET_ALL)
	elif '(NoSuchBucket)' in listbucket:
		print(Fore.MAGENTA+'\b\t[NSB:List Disable]'+Style.RESET_ALL) if domainList else print(Fore.MAGENTA+'[X] No Such Bucket for List files'+Style.RESET_ALL)
	else:
		separator()
		print('\b\t[List Enable]') if domainList else print(listbucket+"\n")
		separator()

def bucket(domain):
	if re.match("^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]))[.]([A-Za-z0-9].|[A-Za-z0-9][A-Za-z0-9\-].*[A-Za-z0-9])$", domain):
		cname = cmd("dig CNAME "+domain+" +short")
		if cname is not None:
			regexp = re.compile(r"\.(s3-.*\.|s3)?(\.(.*)|(s3-.*\.|s3|us-east-2|us-east-1|us-west-1|us-west-2|af-south-1|ap-east-1|ap-south-1|ap-northeast-3|ap-northeast-2|ap-southeast-1|ap-southeast-2|ap-northeast-1|ca-central-1|cn-north-1|cn-northwest-1|eu-central-1|eu-west-1|eu-west-2|eu-south-1|eu-west-3|eu-north-1|sa-east-1|me-south-1|us-gov-east-1|us-gov-west-1))\.amazonaws\.com")
			if regexp.search(cname):
				new_cname = re.sub(r"\.(s3-.*\.|s3)?(\.(.*)|(s3-.*\.|s3|us-east-2|us-east-1|us-west-1|us-west-2|af-south-1|ap-east-1|ap-south-1|ap-northeast-3|ap-northeast-2|ap-southeast-1|ap-southeast-2|ap-northeast-1|ca-central-1|cn-north-1|cn-northwest-1|eu-central-1|eu-west-1|eu-west-2|eu-south-1|eu-west-3|eu-north-1|sa-east-1|me-south-1|us-gov-east-1|us-gov-west-1))\.amazonaws\.com", "", cname)
				new_cname = re.sub(r"\.$", "", new_cname)
				return new_cname
			else:
				r = requests.get('http://'+domain+'.s3.amazonaws.com', verify=False, timeout=20)
				if r.status_code != 404 and r.status_code != 503:
					return domain
				else:
					return 'not_aws'
		else:
			return 'blank_cname'
	else:
		return 'not_domain'

def main():
	banner()

	parser = argparse.ArgumentParser(description='')
	parser.add_argument('-d', '--domain', nargs='?', action="store", help='Target Domain or Subdomain')
	parser.add_argument('-dL', '--domainList', nargs='?', action="store", help="Target Domain/Subdomain list")
	parser.add_argument('-t', '--test', default=False, action="store_true", help="Test the domain also")
	parser.add_argument('-s', '--silent', default=False, action="store_true", help="No Errors")
	parser.add_argument('-v', '--view', default=False, action="store_true", help="List files bucket")
	parser.add_argument('-u', '--upload', default=False, action="store_true", help="Upload to bucket")
	parser.add_argument('-r', '--remove', default=False, action="store_true", help="Delete file after upload")
	parser.add_argument('-a', '--acl', default=False, action="store_true", help="View ACL configuration")
	parser.add_argument('-p', '--policy', default=False, action="store_true", help="View bucket policy")
	parser.add_argument('-c', '--cors', default=False, action="store_true", help="View CORS configuration")
	parser.add_argument('-rP', '--replication', default=False, action="store_true", help="View replication configuration")
	parser.add_argument('-w', '--website', default=False, action="store_true", help="View website configuration")
	parser.add_argument('-l', '--location', default=False, action="store_true", help="View bucket location")
	parser.add_argument('--all', dest='all', default=False, action="store_true", help="View ALL configuration")
	args = parser.parse_args()

	try:
		if args.domain and args.domainList:
			print(Fore.RED+"[X] This Option should not be together!"+Style.RESET_ALL)
			sys.exit(-1)

		elif args.domain:
			if bucket(args.domain) == 'not_domain': 
				print(Fore.RED+"[X] "+args.domain+" is not a Valid Domain!"+Style.RESET_ALL)
				sys.exit(-1)
			if bucket(args.domain) == 'blank_cname':
				print(Fore.RED+"[X] "+args.domain+" has no CNAME!"+Style.RESET_ALL)
				sys.exit(-1)
			if bucket(args.domain) == 'not_aws':
				print(Fore.RED+"[X] "+args.domain+" is not a valid bucket!"+Style.RESET_ALL)
				sys.exit(-1)
			domain = bucket(args.domain)
			print("[+] "+domain+" is valid bucket!") if args.domain == domain else print("[+] "+args.domain+" is valid with a bucket name: "+domain+"!")

			if args.silent: print(Fore.YELLOW+"[!] Sorry, -s or --silent option has no power here :)"+Style.RESET_ALL)

			if args.view: 
				listbucket(domain)
				if args.test and domain != args.domain: listbucket(args.domain)

			if args.upload and args.remove: 
				upload(domain, args.remove)
				if args.test and domain != args.domain: upload(args.domain, args.remove)

			elif args.upload: 
				upload(domain)
				if args.test and domain != args.domain: upload(args.domain)

			elif args.remove: 
				print(Fore.RED+"[X] Please include -u or --upload option!"+Style.RESET_ALL); sys.exit(-1)

			if args.all:
				listbucket(domain)
				acl(domain)
				policy(domain)
				cors(domain)
				replication(domain)
				website(domain)
				location(domain)
				if args.test and domain != args.domain: listbucket(args.domain)
				if args.test and domain != args.domain: acl(args.domain)
				if args.test and domain != args.domain: policy(args.domain)
				if args.test and domain != args.domain: cors(args.domain)
				if args.test and domain != args.domain: replication(args.domain)
				if args.test and domain != args.domain: website(args.domain)
				if args.test and domain != args.domain: location(args.domain)				
			else:
				if args.acl: 
					acl(domain)
					if args.test and domain != args.domain: acl(args.domain)
				if args.policy: 
					policy(domain)
					if args.test and domain != args.domain: policy(args.domain)
				if args.cors: 
					cors(domain)
					if args.test and domain != args.domain: cors(args.domain)
				if args.replication: 
					replication(domain)
					if args.test and domain != args.domain: replication(args.domain)
				if args.website: 
					website(domain)
					if args.test and domain != args.domain: website(args.domain)
				if args.location: 
					location(domain)
					if args.test and domain != args.domain: location(args.domain)

		elif args.domainList:
			if os.path.isfile(args.domainList) == True:
				domains = set(open(args.domainList, 'r'))
				count = len(domains)
				print(Fore.BLACK+Back.WHITE+"Domain Count: "+str(count)+Style.RESET_ALL)
			else:
				print(Fore.RED+"[X] WTF is this bro? I said domain/subdomain list!"+Style.RESET_ALL)
				sys.exit(-1)
			if args.test: print(Fore.YELLOW+"[!] Sorry, -t or --test option has no power here :)"+Style.RESET_ALL)
			for domain in domains:
				domain_list = domain.replace('\n', '')

				if bucket(domain_list) == 'not_domain': 
					if args.silent is False: print(Fore.RED+"[X] "+domain_list+" is not a Valid Domain!"+Style.RESET_ALL)
					continue
				elif bucket(domain_list) == 'blank_cname':
					if args.silent is False: print(Fore.RED+"[X] "+domain_list+" has no CNAME!"+Style.RESET_ALL)
					continue
				elif bucket(domain_list) == 'not_aws':
					if args.silent is False: print(Fore.RED+"[X] "+domain_list+" is not a valid bucket!"+Style.RESET_ALL)
					continue
				else:
					d = bucket(domain_list)
					print("[+] "+d) if domain_list == d else print("[+] "+domain_list+" :: "+d)

				if args.view: listbucket(d, args.domainList)

				if args.upload and args.remove: 
					upload(d, args.remove, args.domainList)
				elif args.upload: 
					upload(d, args.domainList)
				elif args.remove: 
					print(Fore.RED+"[X] Please include -u or --upload option!"+Style.RESET_ALL)

				if args.all:
					listbucket(d, args.domainList)
					acl(d, args.domainList)
					policy(d, args.domainList)
					cors(d, args.domainList)
					replication(d, args.domainList)
					website(d, args.domainList)
					location(d, args.domainList)
				else:
					if args.acl: acl(d, args.domainList)
					if args.policy: policy(d, args.domainList)
					if args.cors: cors(d, args.domainList)
					if args.replication: replication(d, args.domainList)
					if args.website: website(d, args.domainList)
					if args.location: location(d, args.domainList)
		else:
			print(Fore.RED+"[X] Wrong Argument, Go Home!, your drunk Asshole!"+Style.RESET_ALL)
			sys.exit(-1)
	except KeyboardInterrupt:
		print(Fore.RED+"\nKeyboard Interrupt....\nExiting!"+Style.RESET_ALL)
		sys.exit(-1)

if __name__ == "__main__":
	main()

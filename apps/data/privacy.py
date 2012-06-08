"""Routines for protecting anonymity of users and rumormongers"""
import hashlib,re

#If you change this, comparing anonomyzed emails to see if they are the same person becomes slightly more complicated  
allowed_domains = ('gmail.com','yahoo.com','etc.cz',)
re_email = re.compile('[\w._+]+@[\w.]+')
re_email_domain = re.compile('[\w.]+$')

def anonymize_email_body(email_body):
	for email_addy in set(re_email.findall(email_body)):
		email_domain = re_email_domain.search(email_addy).group()
		email_hash = hashlib.sha1(email_addy).hexdigest()
		anon_email = '%s@%s' % (email_hash,email_domain) if email_domain in allowed_domains else email_hash
		email_body = email_body.replace(email_addy,anon_email)
	return email_body




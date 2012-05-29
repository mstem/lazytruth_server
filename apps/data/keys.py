import hashlib, inspect, re


whitespace = re.compile(r"\s+")

whitespace = re.compile(r"[^A-za-z0-9]")
class HashPipe:
	def __valid_lines__(self,text):
		for line in text.splitlines():
			#This needs to be a lot smarter. 
			#if line.find(':') == 3 or line.strip().endswith(':'):
			#	continue
			yield line
	def __split__(self,text):
		return '\n'.join(self.__valid_lines__(text))
	def __hash__(self,text):
		return hashlib.sha224(text.encode('utf-8')).hexdigest()
		#return text
	def _nowhitespace(self,text):
		text = self.__split__(text)
		text =  whitespace.sub("", text)
		return self.__hash__(text)
	def _nowhitespaceplain(self,text):
		text = self.__split__(text)
		text =  whitespace.sub("", text)
		return text
	def _exact(self,text):
		text = self.__split__(text)
		return self.__hash__(text)
	def get_keys(self,text):
		keys = dict()
		text = self.__split__(text)
		for k,f in inspect.getmembers(self):
		    if k.startswith('_') and not k.startswith('__'):
		    	keys[k.lstrip('_')] = f(text)
		print keys
		return keys

hashpipe = HashPipe()

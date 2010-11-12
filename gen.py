#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Appcelerator Documentation Guides
#
# Generate guides webpages
#

import os, sys, shutil, codecs, StringIO, re

try: 
	import json
except: 
	import simplejson as json

try:
	from mako.template import Template
	from mako.lookup import TemplateLookup
except:
	print "Crap, you don't have mako!\n"
	print "Easy install that bitch:\n"
	print ">  easy_install Mako"
	print
	sys.exit(1)
try:
	import markdown
except:
	print "Crap, you don't have markdown!\n"
	print "Easy install that bitch:\n"
	print ">  easy_install ElementTree"
	print ">  easy_install Markdown"
	print
	sys.exit(1)

template_dir = os.path.abspath(os.path.dirname(sys._getframe(0).f_code.co_filename))
root_dir = os.path.join(template_dir,'../')
doc_json_file = os.path.join(template_dir,'doc.json')
doc_json = json.loads(codecs.open(doc_json_file,encoding='utf-8').read())
out_dir = os.path.join(template_dir,'output')
if not os.path.exists(out_dir):
	os.makedirs(out_dir)
templates_dir = os.path.join(template_dir,'templates')
guides = doc_json['guides']
statics = doc_json['statics']
languages = doc_json['languages']
sections = []
globals = {}

def make_link(text):
	return text.replace(' ','_').lower()

def extract_summary(line):
	begin_tag = '<summary>'
	end_tag = '</summary>'
	idx = line.find(begin_tag)
	if idx == -1:
		return (None,line)
	idx2 = line.find(end_tag,idx)
	begin = line[0:idx]
	end = line[idx2+len(end_tag):]
	result = begin + end
	data = line[idx+len(end_tag):idx2].strip()
	data = markdown.markdown(data, extensions=['fenced_code'],
							output_format='xhtml1')
	return (data,result)
	
def transform_content(line,title,remove=True,replace=True):
	begin_tag = '<%s>' % title
	end_tag = '</%s>' % title
	idx = line.find(begin_tag)
	if idx == -1:
		return line
	idx2 = line.find(end_tag,idx)
	
	data = line[idx+len(begin_tag):idx2].strip()
	data = markdown.markdown(data, extensions=['fenced_code'],
							output_format='xhtml1')
	
	begin = line[0:idx]
	end = line[idx2+len(end_tag):]
	result =  begin + '<div class="%s"><p>' % title 
	result += data + '</p></div>' + end
	
	return transform_content(result,title,remove,replace)
	
def tickerize(line):
	idx = line.find('`')
	if idx == -1:
		return line
	idx2 = line.find('`',idx+1)
	# Prevent infinite loops of doooooooom.
	if idx2 < idx:
		print("Malformed doc file! Missing a second backtick in: %s" % line)
		sys.exit(1)
	token = line[idx+1:idx2]
	if token.startswith("Titanium.") or token.startswith("Ti."):
		content = "<a href=\"http://developer.appcelerator.com/apidoc/mobile/latest/%s.html\">%s</a>" % (token,token)
	else:
		content = "<tt>%s</tt>" % token
	return tickerize(line[0:idx] + content + line[idx2+1:])

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }
def html_escape(text):
    return "".join(html_escape_table.get(c,c) for c in text)	

def anchorize(line):
	idx = line.find('[[')
	if idx == -1:
		return line
	idx2 = line.find(']]',idx+2)
	anchor = line[idx+2:idx2] 
	before = line[0:idx-1] + ' '
	after = line[idx2+2:]
	if anchor.startswith("Titanium.") or anchor.startswith("Ti."):
		content = "<a href=\"http://developer.appcelerator.com/apidoc/mobile/latest/%s.html\">%s</a>" % (anchor,anchor)
	else:
		content = "<a href=\"%s.html\">%s</a>" % (anchor,anchor)
	result = before + content + after
	return anchorize(result)

def colorize_code(line,offset=0):
	idx = line.find("<code",offset)
	if idx == -1:
		return line
	endi = line.find(">",idx)
	idx2 = line.find("</code>",idx)
	code = line[idx+6:idx2]
	before = line[0:idx]
	after = line[idx2+7:]
	html = html_escape(line[endi+1:idx2])
	result = line[idx:endi+1].replace('code','CODE') + html + '</CODE>'
	
	content = before + '<div class="code_container">' + result + '</div>' + after
	return colorize_code(content,idx2)

def fix_codeblock(line):
	idx = line.find("<pre><code")
	if idx == -1:
		# default to javascript
		return line.replace('<code>','<code class="javascript">')
	idx2 = line.find(">",idx+10)
	endi = line.find("</code></pre>",idx2)
	before = line[0:idx]
	after = line[endi+13:]
	html = '<div class="code_container">' + line[idx+5:idx2] + line[idx2:idx2+1] + '\n' + line[idx2+1:endi] + '</code></div>\n'
	return fix_codeblock(before + html + after)

def generate_template(source,guide,language,language_code,language_dir,languages,sections):	
	print "Generating %s (%s)" % (guide['source'],language)
	
	template = 'guide.html'
	if 'template' in guide:
		template = guide['template']
	
	template_body = codecs.open(os.path.join(templates_dir,template),encoding='utf-8').read()
		
	source_in = codecs.open(source,encoding='utf-8').read()	

	# basic pre-processing
	source_in = tickerize(source_in)
	source_in = anchorize(source_in)
	source_in = colorize_code(source_in)
	source_in = source_in.replace('CODE','code')

	# special tags
	(summary,source_in) = extract_summary(source_in)

	for name in ('warning','note','info'):
		source_in = transform_content(source_in,name,False,True)

	xhtml = markdown.markdown(source_in, extensions=['fenced_code'],
							output_format='xhtml1')

	xhtml = fix_codeblock(xhtml)

	toc = []
	cur = None
	for i in re.finditer("<h([1-2])>(.*)</h[1-2]>",xhtml):
		level = i.group(1)
		text = i.group(2)
		if level == '1':
			cur = {'title':text,'children':[],'link':make_link(text)}
			toc.append(cur)
		else:
			cur['children'].append({'title':text,'link':make_link(text)})
		
	for t in toc:
		xhtml = xhtml.replace('<h1>%s</h1>' % t['title'], '<h3 id="%s">%s</h3>' % (t['link'],t['title']))
		for c in t['children']:
			xhtml = xhtml.replace('<h2>%s</h2>' % c['title'], '<h4 id="%s">%s</h4>' % (c['link'],c['title']))
		
	lookup = TemplateLookup(directories=[templates_dir], module_directory=templates_dir)	
	output = Template(template_body,lookup=lookup).render_unicode(summary=summary,
												toc=toc,
												body=xhtml,
												title=guide['name'],
												guides=guides,
												language=language,
												language_code = language_code,
												languages = languages,
												sections = sections,
												template_dir = template_dir,
												globals = globals,
												description=guide['description'])
												
	if not os.path.exists(os.path.join(out_dir,language_dir)):
		os.makedirs(os.path.join(out_dir,language_dir))
		
	file = os.path.join(out_dir,language_dir,'%s' % guide['source'].replace('.md','.html'))
	f = codecs.open(file,'w',encoding='utf-8')
	f.write(output)
	f.close()

def generate_static(static,language,language_code,language_dir,generate_if_not_found=False):
	source = static['source']
	file = os.path.join(template_dir,'source',language_dir,source)
	if not os.path.exists(file) and generate_if_not_found:
		file2 = os.path.join(template_dir,'source',source)
		if os.path.exists(file2):
			file = file2
		else:
			print "Couldn't find %s at %s or %s" % (static,file,file2)
			print "Skipping generation..."
			return
	generate_template(file,static,language,language_code,language_dir,languages,sections)
	
def generate_guide(guide,language,language_code,language_dir,generate_if_not_found=False):	
	source = os.path.join(template_dir,'source',language_dir,guide['source'])
	if not os.path.exists(source) and generate_if_not_found:
		print "Couldn't find source: %s" % source 
		print "Generating an empty file at %s" % source
		s = codecs.open(source,'w',encoding='utf-8')
		X="""<summary>
This page has not yet been developed.  Help [[contribute]] by writing documentation.
</summary>"""
		s.write(X)
		s.close()
	generate_template(source,guide,language,language_code,language_dir,languages,sections)

def get_language(lang):
	for language_entry in languages:
		language = language_entry['title']
		language_dir = language_entry['directory']
		language_code = language_entry['code']
		if language_code == lang:
			return language,language_dir,language_code
	print "Couldn't find language: %s" % lang
	sys.exit(1)
	
def main(args):
	if os.path.exists(os.path.join(out_dir,'assets')):
		shutil.rmtree(os.path.join(out_dir,'assets'))
	shutil.copytree(os.path.join(template_dir,'assets'),os.path.join(out_dir,'assets'))
	
	
	# add any key=value pair as a global so that they can be picked up in template
	for arg in args:
		i = arg.find('=')
		if i == -1: continue
		k,v = arg.split('=')
		globals[k]=v

	lang = 'en'
	if globals.has_key('lang'):
		lang = globals['lang']
	language, language_code, language_dir = get_language(lang)

	if globals.has_key('guide'):
		found = False
		guide = globals['guide']
		for entry in doc_json['guides']:
			if entry['source']==guide:
				found = True
				break
		if not found:
			print "No guide found: %s" % guide
			sys.exit(1)
		else:
			generate_guide(entry,language,language_code,language_dir)
			sys.exit(0)

	if globals.has_key('static'):
		found = False
		static = globals['static']
		for entry in doc_json['statics']:
			if entry['source']==static:
				found = True
				break
		if not found:
			print "No static entry found: %s" % static
			sys.exit(1)
		else:
			generate_static(entry,language,language_code,language_dir)
			sys.exit(0)

	for entry in guides:
		section = entry['section']
		
		found = False
		
		for x in sections:
			if x['title'] == section:
				x['books'].append(entry)
				found = True

		if not found:
			sections.append({'title':section,'books':[entry]})		
		
	for language_entry in languages:
		language = language_entry['title']
		language_dir = language_entry['directory']
		language_code = language_entry['code']
		
		if not os.path.exists(os.path.join(template_dir,'source',language_dir)):
			print "Skipping generation of language: %s" % language
			print "No language directory found at: %s" % os.path.join(template_dir,'source',language_dir)
			continue

		for static in statics:
			generate_static(static,language,language_code,language_dir,True)
	
		for guide in guides:
			generate_guide(guide,language,language_code,language_dir,True)
	

if __name__ == '__main__':
	main(sys.argv)

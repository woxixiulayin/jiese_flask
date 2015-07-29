# !coding:utf-8
from models import *
from datetime import datetime
import codecs,re,os,chardet
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

dir_cur = os.getcwd()

class myfile(object):
	def __init__(self, path):
		self.path = path
		self.lines = []
		# with codecs.open(path, 'r',  encoding='utf-8') as f:
		# f = open(self.path)
		# for line in f.readlines():
		# 	if len(line) > 1:
		# 		self.lines.append(line)

	def insert():
		pass

	def predeal():
		pass

class quotation(myfile):
	quotations = []
#quotation start with number
#total 1005
	def predeal(self):
		p = re.compile(r'(^\d)(\.)(.*$)')
		for line in self.lines:
			m = p.match(line)
			if  m!= None:
				quo = Quotion_doc()
				quo['content'] = m.group(3)
				author = "飞翔戒色语录"
				quo['author'] = author
				quo['rep_num'] = 0
				quo['last_time'] = ""
				quotations.append(quo)

	def insert(self):
		for quo in quotations:
			quo.save()

class jieweiliangyao_post(myfile):
	def predeal(self):
		self.post = Post_doc()
		self.post.author = "飞翔"
		self.post.first_time = datetime.now().strftime( '%c' )
		self.post.last_time = self.post.first_time
		self.post.title = ""
		self.post.tags.append("戒为良药")
		self.post.rep_num = 0
		self.post.body = ""
		p = re.compile(r'(.*)(\.txt$)')
		m = p.match(self.path)
		self.post.title = m.group(1)
		for line in self.lines:
			self.post.body += line

	def insert(self):
		self.post.save()


#only start with number
def insertjieweiliangyao(dir):
	files = os.listdir(dir)
	p = re.compile(r'(.*)(\.txt$)')
	for fi in files:
		m = p.match(fi)
		if m != None:
			fpath = dir + '/' + fi
			ipath = unicode(fpath , "utf8")
			post = jieweiliangyao_post(fi)
			with open(ipath, 'r') as o:
				#detect doc encoding used fir different open
				codedetect = chardet.detect(o.readline())["encoding"]
			#use  errors='ignore' to avoid errors when some issue happen
			with codecs.open(ipath, 'r',  encoding=codedetect, errors='ignore') as f:
				for line in f.readlines():
					post.lines.append(line.decode('utf-8'))
			post.predeal()
			if len(Post_doc.objects(title=post.post.title)) == 0:
				print post.post.title
				post.post.save()
				print 'save sucessfully'
	print len(Post_doc.objects())


# 	f = codecs.open(path, 'r',  encoding='utf-8')
# 	# for line in f.readlines():
# 	# 	print line
# 	# 	linelist.append(line)
# 	return f.read()


if __name__ == '__main__':
	# f = quotation("/home/gang/work/python/web/jiese_flask/mymongofunc/resource/jieseyulu.txt")
	# f.predeal()

	# num = 0
	# for quo in Quotion_doc.objects():
		# quo.index = num
		# quo.save()
		# num += 1
		# print quo.index
	# print num
	# f = jieweiliangyao_post("./jiesedir/test.txt")
	# f.predeal()
	# print f.post.body
	# insertjieweiliangyao(dir_cur + '/resource/jiesedir')
	# ipath = '/home/gang/work/python/web/jiese_flask/mymongofunc/resource/jiesedir/16【飞翔经验：遗精问题补充、无害论、禁欲有害论、婚后次数】16季.txt'
 # 	ipath = unicode(ipath , "utf8")
 	# fn = open(ipath)

 	for p in Post_doc.objects():
 		print p.title

# encoding:utf-8 
#!python3

'''
创建新文件：
将文本复制再运行本脚本选择生成.py .pyui .text文件，在本程序主目录生成自定义文件名的新文件。方便的解决了导入py文本文件的问题，更适合pythonista3 v.3.1以下版本的导入py或pyui脚本所用，同时也可将文本保存为text文本把pythonista当记事本使用。encode('utf-8')
@honzou
2018/06/01
'''
import appex
import clipboard
import console
import shutil
import os,codecs
#reload(sys) 
#sys.setdefaultencoding('utf-8')

def getuniquename(filename, ext):
	root, extension = os.path.splitext(filename)
	if ext!='':
		extension = ext
	filename = root + extension
	filenum = 1
	while os.path.isfile(filename):
		filename = '{} {}{}'.format(root, filenum, extension)
		filenum += 1
	return filename
	
def main():
	console.clear()
	dest_path_short = '~/Documents'
	dest_path = os.path.expanduser(dest_path_short)
	if not os.path.isdir(dest_path):
		print('Create ' + dest_path_short)
		os.mkdir(dest_path)
	if not appex.is_running_extension():
		print('正在获取剪贴板文本...')
		txt = clipboard.get()
		tet =txt.encode('utf-8')#转码
		#print(tet)
		text = tet.decode("utf-8")
		#print (text)
		
		
		assert text, '剪贴板没有文本内容!'
		resp = console.alert('honzou友情提示', '请选择新建文件的类型：', '.py', '.pyui','.text', hide_cancel_button=False)
		if resp==1:
			ext = '.py'
		elif resp==2:
			ext = '.pyui'
		elif resp==3:
			ext = '.text'
		clipboards = input('创建文件名：')
		filename=os.path.join(dest_path,clipboards)
		filename=getuniquename(filename,ext)
		while os.path.isfile(filename):
			filename = '{} {}{}'.format(root, filenum, extension)
			filenum += 1
		with codecs.open(filename,'w','utf-8') as f:         #再次定义文本编码
			
			f.write(text)
		print('成功写入!')
	else:
		file = appex.get_file_path()
		print('Input path: %s' % file)
		filename=os.path.join(dest_path, os.path.basename(file))
		filename=getuniquename(filename,'')
		shutil.copy(file,filename)
	print('文件已保存到 %s' % dest_path_short)
	if not os.path.exists(filename):
		print(' > Error file %s not found !' % os.path.basename(filename))
	else:
		print('请到该目录查看文件：%s' % os.path.basename(filename))
		
if __name__ == '__main__':
	main()

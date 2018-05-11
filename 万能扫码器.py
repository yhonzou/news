#!python3
# coding: utf-8
'''
扫描二维码后点击页面左上角x直接跳转到safari打开
支持微信，qq，支付宝，节点添加及网页等跳转打开
@honzou改编
2018/05/11
'''

from objc_util import *
from ctypes import c_void_p
import ui,clipboard,console
import sound,webbrowser

found_codes = set()
main_view = None

AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureMetadataOutput = ObjCClass('AVCaptureMetadataOutput')
AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')
dispatch_get_current_queue = c.dispatch_get_current_queue
dispatch_get_current_queue.restype = c_void_p

def captureOutput_didOutputMetadataObjects_fromConnection_(_self, _cmd, _output, _metadata_objects, _conn):
	objects = ObjCInstance(_metadata_objects)
	for obj in objects:
		s = str(obj.stringValue())
		if s not in found_codes:
			found_codes.add(s)
			sound.play_effect('digital:PowerUp7')
		main_view['label'].text = '请点击👆ㄨ跳转:   ' + s

MetadataDelegate = create_objc_class('MetadataDelegate', methods=[captureOutput_didOutputMetadataObjects_fromConnection_], protocols=['AVCaptureMetadataOutputObjectsDelegate'])

@on_main_thread
def main():
	global main_view
	delegate = MetadataDelegate.new()
	main_view = ui.View(frame=(0, 0, 400, 600))#400,600为扫描器显示范围
	main_view.name = '万能扫码器'
	session = AVCaptureSession.alloc().init()
	device = AVCaptureDevice.defaultDeviceWithMediaType_('vide')
	_input = AVCaptureDeviceInput.deviceInputWithDevice_error_(device, None)
	if _input:
		session.addInput_(_input)
	else:
		print('Failed to create input')
		return
	output = AVCaptureMetadataOutput.alloc().init()
	queue = ObjCInstance(dispatch_get_current_queue())
	output.setMetadataObjectsDelegate_queue_(delegate, queue)
	session.addOutput_(output)
	output.setMetadataObjectTypes_(output.availableMetadataObjectTypes())
	prev_layer = AVCaptureVideoPreviewLayer.layerWithSession_(session)
	prev_layer.frame = ObjCInstance(main_view).bounds()
	prev_layer.setVideoGravity_('AVLayerVideoGravityResizeAspectFill')
	ObjCInstance(main_view).layer().addSublayer_(prev_layer)
	label = ui.Label(frame=(0, 0, 400, 40), flex='W', name='label')#40为label的宽度
	label.background_color = (0, 0, 0, 0.2)#透明度
	label.text_color = 'white'
	label.text = '请扫描二维码'
	label.alignment = ui.ALIGN_CENTER
	main_view.add_subview(label)
	session.startRunning()
	main_view.present('sheet')
	main_view.wait_modal()
	session.stopRunning()
	delegate.release()
	session.release()
	output.release()
	if found_codes:
		url= '\n'.join(found_codes)
		url1= str.lower(url)
		#将所有链接都转换为小写str.upper()改为大写
		
		if 'wechat' in url:
			webbrowser.open('weixin://scanqrcode')
		elif 'alipay' in url1:
			webbrowser.open('alipays://platformapi/startapp?saId=10000007')
		elif 'qq.com' in url:
			if 'weixin.qq.com' in url:
				webbrowser.open('weixin://scanqrcode')
			else:
				webbrowser.open('mqqapi://qrcode/scan_qrcode?version=1&src_type=app')
		elif 'weibo' in url:
			webbrowser.open('weibo://qrcode')
		elif 'ssr:' in url:
			webbrowser.open(url)
		elif 'ss:' in url:
			webbrowser.open(url)
			
			
		else:
			if 'http' in url:
				webbrowser.open_new('safari-'+url)
			else:
				console.alert('⚠️ 该二维码已失效')
			#break

if __name__ == '__main__':
	main()
"""URL Parsing Module"""
import urllib.request
import threading
import multiprocessing
import time

def url_page_download(url, filename):
	html = urllib.request.urlopen(url).read()
	fd = open(html_file_path + filename, "wb")
	fd.write(html)
	fd.close()
	# print (html)


def html_page_parse(filename):
	# print(html_file_path)
	fd = open(html_file_path + filename,'r')
	flag = 0
	list_ = []
	while True:
		line = fd.readline()
		# print(line)
		if line.find('Latest News') != -1:
			flag = 1
		if line[-21:-6] == 'Upcoming Events' :
			return list_
		if line.find('http://') != -1 and flag == 1:
			link = line.lstrip(" <a href=")
			linkr = link[0:link.find('">')]
			linkl =linkr.lstrip('"')
			list_.append(linkl)
		if(len(line) <= 0 ):
			break


def sub_url_thread_func(url):
	print(threading.current_thread().getName(), 'Starting')
	url_page_download(url, 'thread_download/' + threading.current_thread().getName() +'.html')
	time.sleep(1)
	print(threading.current_thread().getName(), 'Exiting')
	print('Threading URL ->', url)


def sub_url_process_func(url, pro_no):
	print('Process', pro_no, 'Starting')
	url_page_download(url, 'process_download/Process-' + str(pro_no) +'.html')
	time.sleep(1)
	print('Process ', pro_no, 'Exiting')
	print('Multiprocessing URL ->', url)


def main():
	global html_file_path
	url = 'https://www.python.org'
	html_file_path = '/'.join(__file__.split('/')[0:-1]) + '/'
	# url_page_download(url, 'download_html.html')
	url_list = html_page_parse('download_html.html')

	for url in url_list:
		thread = threading.Thread(target=sub_url_thread_func, args=(url,))
		thread.start()
		# thread.join()

	process_no = 1
	for url in url_list:
		process = multiprocessing.Process(target=sub_url_process_func, args=(url,process_no))
		process.start()
		# process.join()
		process_no += 1

if __name__ == "__main__":
	main()
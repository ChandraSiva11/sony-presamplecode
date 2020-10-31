#!/usr/bin/python3
"""Selenium script for web testing"""
from selenium import webdriver
import platform
import re
import threading
import multiprocessing
import time


def web_driver_paths():
    """Constructing the selenium web driver path"""
    global web_driver_path
    global appln_path
    global plat_form
    script_file_path = __file__
    plat_form = platform.system()
    if(plat_form.lower() == 'linux'):
        appln_path = '/'.join(script_file_path.split('/')[0:-1])
        web_driver_path = appln_path + '/driver/chromedriver_linux'
        print(web_driver_path)
    elif(plat_form.lower() == 'windows'):
        appln_path = '\\'.join(script_file_path.split('\\')[0:-1])
        web_driver_path = appln_path + '\\driver\\chromedriver_win32.exe'
        print(web_driver_path)


def home_page_download():
    """Chrome webbrowser opening"""
    driver = webdriver.Chrome(executable_path=web_driver_path)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://python.org')
    time.sleep(1)
    if(plat_form.lower() == 'linux'):
        with open(appln_path + '/page_source.html', "w") as f:
            f.write(driver.page_source)
    elif(plat_form.lower() == 'windows'):
        with open(appln_path + '\\page_source.html', "w") as f:
            f.write(driver.page_source)
    driver.close()


def sub_url_page_download(url, path):
    """Sub URL pages download and store it in a location"""
    driver = webdriver.Chrome(executable_path=web_driver_path)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(url)
    if(plat_form.lower() == 'linux'):
        file_path = appln_path + '/' + path
    elif(plat_form.lower() == 'windows'):
        file_path = appln_path + '\\' + path
    with open(file_path, "w") as f:
            f.write(driver.page_source)
    driver.close()


def html_page_parse():
    """Html page parsing"""
    if(plat_form.lower() == 'linux'):
        fd = open(appln_path + '/page_source.html','r')
        lines = fd.read()
        fd.close()
    elif(plat_form.lower() == 'windows'):
        fd = open(appln_path + '\\page_source.html','r')
        lines = fd.read()
        fd.close
    start_index = lines.find('Latest News')
    end_index = lines.find('Upcoming Events')
    match_line = lines[start_index:end_index]
    matched = re.findall('https?://.*html?',str(match_line))
    print(matched)
    return matched


def sub_url_thread_process(url, pro_no, Pro_the):
    """Python thread and process processing common file"""
    print('Process or thread', pro_no, 'Starting')
    sub_url_page_download(url,Pro_the  + '_down/' +Pro_the + str(pro_no) +'.html')
    time.sleep(1)
    print('Process or thread ', pro_no, 'Exiting')


def main():
    """Doc string of main script"""
    web_driver_paths()
    # home_page_download()
    url_list = html_page_parse()

    thread_no = 1
    for url in url_list:
        thread = threading.Thread(target=sub_url_thread_process, args=(url,thread_no, 'Thread'))
        thread.start()
        # thread.join()
        thread_no += 1

    process_no = 1
    for url in url_list:
        process = multiprocessing.Process(target=sub_url_thread_process, args=(url,process_no, 'Process'))
        process.start()
        # process.join()
        process_no += 1


if __name__ == '__main__':
    main()

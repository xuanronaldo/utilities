from requests import get
from datetime import datetime
from os import listdir, system, getcwd, chdir, path
from sys import platform

date = datetime.now().strftime('%Y-%m-%d')
pic_dir = '/Users/xuanronaldo/wallpaper'


def download_wallpaper(filename, index=0):
    """
    download the wallpaper from Bing to the specified path
    :param filename: the
    :param index: the parameter that the Bing api need.
    :return:
    """
    pic = get('https://bing.biturl.top/?resolution=1920&format=image&index=%s&mkt=zh-CN' % index).content
    file_path = path.join(pic_dir, filename)
    with open(file_path, 'wb+') as f:
        f.write(pic)


def has_download_today():
    return listdir(pic_dir).__contains__(filename)


def set_wallpaper(path):
    cmd = ''
    if platform.lower().__contains__('darwin'):
        # the MacOS's command to change the wallpaper
        cmd = "osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"%s\"'" % path

    system(cmd)


if __name__ == '__main__':
    if not has_download_today():
        filename = date + '.jpg'
        download_wallpaper(filename)
        chdir(pic_dir)
        abs_path = path.join(getcwd(), filename)
        set_wallpaper(abs_path)

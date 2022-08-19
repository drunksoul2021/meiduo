from django.http import HttpResponse
from django.shortcuts import render, redirect
from book.models import BookInfo


# Create your views here.
def create_book(request):

    book = BookInfo.objects.create(
        name='abc',
        pub_date='2022-1-1',
        readcount=10,
    )
    return HttpResponse('create')

def shop(request,city_id,mobile):

    # import re
    # if not re.match('\d{5}',shop_id):
    #     return HttpResponse('no comodity')
    print(city_id,mobile)
    query_params=request.GET
    print(query_params)
    #order=query_params.get('order') #we can get one key one value
    #order=query_params['order']
    #print(order)
    #<QueryDict: {'order': ['readcount']}>
    #< QueryDict: {'order': ['readcount', 'commentcount'], 'page': ['1']} >
    order=query_params.getlist('order') #we can get one key multiple values
    print(order)
    return HttpResponse('my shop')

def register(request):

    data = request.POST
    print(data)
    return HttpResponse("ok")

def json(request):
    #1.
    body = request.body
    print(body)
    print(type(body))
    #b'{"name":"itcast","age":10}'
    #<class 'bytes'>
    #2.
    body_str = body.decode()
    print(body_str)
    print(type(body_str))
    #{"name": "itcast", "age": 10}
    #<class 'str'>
    #JSON str, can be transfer to Python dict
    #3.
    import json
    body_dict = json.loads(body_str)
    print((body_dict))
    print(type(body_dict))

    #############################
    print(request.META)
    #{'PATH': '/home/ww/.virtualenvs/meiduo/bin:/home/ww/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin', 'LC_MEASUREMENT': 'en_US.UTF-8', 'XAUTHORITY': '/run/user/1000/gdm/Xauthority', 'INVOCATION_ID': '6bac8e05c5dd425b8a71311471e54cbf', 'XMODIFIERS': '@im=fcitx', 'LC_TELEPHONE': 'en_US.UTF-8', 'XDG_DATA_DIRS': '/usr/share/ubuntu-xorg:/usr/share/gnome:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop', 'GDMSESSION': 'ubuntu-xorg', 'LC_TIME': 'en_US.UTF-8', 'PAPERSIZE': 'letter', 'GTK_IM_MODULE': 'fcitx', 'DBUS_SESSION_BUS_ADDRESS': 'unix:path=/run/user/1000/bus', 'PS1': '(meiduo) ', 'XDG_CURRENT_DESKTOP': 'ubuntu:GNOME', 'JOURNAL_STREAM': '8:31811', 'LC_PAPER': 'en_US.UTF-8', 'SESSION_MANAGER': 'local/ww:@/tmp/.ICE-unix/1804,unix/ww:/tmp/.ICE-unix/1804', 'USERNAME': 'ww', 'LOGNAME': 'ww', 'PWD': '/home/ww/developmeiduo/meiduo/bookmanage03', 'MANAGERPID': '1531', 'IM_CONFIG_PHASE': '1', 'PYCHARM_HOSTED': '1', 'GJS_DEBUG_TOPICS': 'JS ERROR;JS LOG', 'PYTHONPATH': '/home/ww/developmeiduo/meiduo/bookmanage03:/home/ww/developmeiduo/meiduo/bookmanage03', 'SHELL': '/bin/bash', 'LC_ADDRESS': 'en_US.UTF-8', 'GIO_LAUNCHED_DESKTOP_FILE': '/usr/share/applications/jetbrains-pycharm-ce.desktop', 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated', 'GTK_MODULES': 'gail:atk-bridge', 'VIRTUAL_ENV': '/home/ww/.virtualenvs/meiduo', 'CLUTTER_IM_MODULE': 'fcitx', 'SYSTEMD_EXEC_PID': '1823', 'XDG_SESSION_DESKTOP': 'ubuntu-xorg', 'SSH_AGENT_LAUNCHER': 'gnome-keyring', 'SHLVL': '0', 'LC_IDENTIFICATION': 'en_US.UTF-8', 'LC_MONETARY': 'en_US.UTF-8', 'QT_IM_MODULE': 'fcitx', 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu-xorg:/etc/xdg', 'LANG': 'en_US.UTF-8', 'XDG_SESSION_TYPE': 'x11', 'DISPLAY': ':0', 'LC_NAME': 'en_US.UTF-8', 'XDG_SESSION_CLASS': 'user', '_': '/usr/bin/dbus-update-activation-environment', 'PYTHONIOENCODING': 'UTF-8', 'GPG_AGENT_INFO': '/run/user/1000/gnupg/S.gpg-agent:0:1', 'DESKTOP_SESSION': 'ubuntu-xorg', 'USER': 'ww', 'XDG_MENU_PREFIX': 'gnome-', 'GIO_LAUNCHED_DESKTOP_FILE_PID': '3120', 'QT_ACCESSIBILITY': '1', 'WINDOWPATH': '2', 'LC_NUMERIC': 'en_US.UTF-8', 'GJS_DEBUG_OUTPUT': 'stderr', 'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh', 'PYTHONUNBUFFERED': '1', 'GNOME_SHELL_SESSION_MODE': 'ubuntu', 'XDG_RUNTIME_DIR': '/run/user/1000', 'HOME': '/home/ww', 'DJANGO_SETTINGS_MODULE': 'bookmanage03.settings', 'TZ': 'UTC', 'RUN_MAIN': 'true', 'SERVER_NAME': 'localhost', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8002', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '26', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'POST', 'PATH_INFO': '/json/', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'application/json', 'HTTP_ACCEPT': '*/*', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_USER_AGENT': 'ApiPOST Runtime +https://www.apipost.cn', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_HOST': '127.0.0.1:8002', 'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0xffffbb2e9030>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>}
    print(request.META['SERVER_PORT'])
    return HttpResponse('json')

def method(request):

    print(request.method)

    return HttpResponse('method')

from  django.http import HttpResponse,JsonResponse

def response(request):
    # response = HttpResponse('res', status=200)
    #
    # response['name']='itcast'
    #
    # return response
    info = {
        'name':'kaihua',
        'address':'singapore'
    }

    girl_friends = [
        {
            'name':'rose',
            'address': 'au'
        },
        {
            'name':'jack',
            'address':'us'
        }
    ]
    # data return type of dict
    # safe = Ture means data is dict_data
    # JsonResponse can convert dict to json
    # response =JsonResponse(data=girl_friends,safe=False)
    # return response
    # import json
    # data = json.dumps(girl_friends)
    #
    # response = HttpResponse(data)
    # return response

    return redirect('http://drunksoul.3vcm.vip')


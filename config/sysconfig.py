# -*-coding:utf-8 -*-
# author: zeyang@staff.sina.com.cn
# time:   2013-12-12

import os
_WORKSPACE = os.getcwd()

# test app information.
SOURCE = "4125898983"
ACCESS_TOKEN = "2.00mG98WBnnqNVEfe7acc1871Kgp6XC"

# api reference information
apiRef = {
'status':
	{'apis': ['queryid','querymid','show'],
	'name': '微博组接口',
	'apipath': _WORKSPACE + '/data/api/status',
	'casepath': _WORKSPACE + '/data/case/status'},
'open':
	{'apis': [],
	'name': '平台组接口',
	'apipath': _WORKSPACE + '/data/api/open',
	'casepath': _WORKSPACE + '/data/case/open'},
'oauth':
	{'apis':[],
	'name':'授权组接口',
	'apipath':_WORKSPACE + '/data/api/oauth',
	'casepath': _WORKSPACE + '/data/case/oauth'}
}

# work dict path
_PLANPATH = _WORKSPACE + '/plan'
_APIPATH = _WORKSPACE + '/data/api'
_CASEPATH = _WORKSPACE + '/data/case'

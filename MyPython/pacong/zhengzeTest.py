# -*- coding:utf-8 -*-
'''
Created on 2016-8-11

@author: 
'''

import re
a = re.findall(r'<article>+(.+)</article>+', '<article>2343423</article>' )
print a
b = re.findall(r'<article>+([\s\S]*)</article>+', '<article>阿斯顿撒ffff大苏打</article>' )
print b
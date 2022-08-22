"""
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""


def front_back(str):
	m_str = str[1:len(str) - 1]
	f_str = str[:1]
	l_str = str[len(str) - 1]
	
	if len(str) == 1:
		return str
	elif len(str) == 2:
		return l_str + f_str
	else:
		return l_str + m_str + f_str
		

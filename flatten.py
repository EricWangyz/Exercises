from collections.abc import *

def flatten(lst, out_lst=None):
	if out_lst is None:
		out_lst = []
	for i in lst:
		if isinstance(i, Iterable):
			flatten(i, out_lst)
		else:
			out_lst.append(i)
	return out_lst
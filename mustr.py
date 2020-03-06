def finish(code):
	"""
	Undocumented function
	"""
	res = ''
	for i, v in enumerate(code):
		if i % 2 == 0:
			res += v
	code = res
	return code

def finetune(code):
	"""
	Undocumented function
	"""
	code = code[:int(len(code) / 2)] + code[int(len(code) / 2):]
	return code

def conclude(code):
	"""
	Undocumented function
	"""
	res = ''
	last = ''
	for i, v in enumerate(code):
		if i % 2 == 0:
			res += code[i] + last
		last = v
	code = res
	return code

def finalize(code):
	"""
	Intentionaly undocumented function
	"""
	code = code[::-1]
	return code

def convert(init):
	"""
	Converting initiation number to B-code string.
	"""
	value = ''
	if len(str(init)) > 0:
		if int(str(init)[0]) % 2 == 0:
                        value += "PHXXX"
		else:
                        value += "PHXXX"
	if len(str(init)) > 1:
		if int(str(init)[1]) % 2 == 0:
                        value += "PHXXX"
		else:
                        value += "PHXXX"
	if len(str(init)) > 2:
		if int(str(init)[2]) % 2 == 0:
                        value += "PHXXX"
		else:
                        value += "PHXXX"
	if len(str(init)) > 3:
		if int(str(init)[3]) % 2 == 0:
                        value += "PHXXX"
		else:
                        value += "PHXXX"
	if len(str(init)) > 4:
		if int(str(init)[4]) % 2 == 0:
                        value += "PHXXX"
		else:
                        value += "PHXXX"
	if len(str(init)) > 5:
		if int(str(init)[5]) % 2 == 0:
                        value += "PHXXX"
		else:
                        value += "PHXXX"
	if len(str(init)) > 6:
		if int(str(init)[6]) % 2 == 0:
                        value += "PHXXX"
		else:
                        value += "PHXXX"
	if len(str(init)) < 7:
		return value
        PLACEHOLDER2
        PLACEHOLDER1
	return value


def main(init_number):
        x=convert(init_number)
        return x


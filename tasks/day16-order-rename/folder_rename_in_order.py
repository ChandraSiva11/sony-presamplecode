"""Module Doc string"""
import os


def main():
	path = '/'.join(__file__.split('/')[0:-1])+'/file_folder/'
	list_ = os.listdir(path)
	indx_val = 0
	print('Orginal file names before chage --> ',list_)
	for file in list_:
		li_ = file.split('-')
		if(len(li_[0]) < 2):
			print(file)
			li_[0] = li_[0].zfill(2)
			print('-'.join(li_))
			list_[indx_val] = '-'.join(li_)
			if os.path.isfile(path + list_[indx_val]):
				os.rename(path + file, path + list_[indx_val] + '-')
			else:
				os.rename(path + file, path + list_[indx_val])
			# Rename command wants to write
		indx_val += 1

	list_.sort()
	print('Before Duplicate Rename --> ', list_)
	for num in range(1, len(list_) + 1):
		# print("list no", num, 'list ->', list_[num - 1])
		li_ = list_[num - 1].split('-')
		if(len(li_) == 2 ):
			if num != int(li_[0]):
				print(num, li_)
				li_[0] = str(num).zfill(2)
				if os.path.isfile(path + '-'.join(li_)):
					os.rename(path + list_[num -1 ], path + '-'.join(li_) + '-')
				else:	
					os.rename(path + list_[num -1 ], path + '-'.join(li_))
				list_[num -1 ] = '-'.join(li_)
				# Rename command
	print('After Duplicate Rename --> ',list_)


if __name__ == '__main__':
	main()
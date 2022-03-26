import re, glob, os

name_ptrn = re.compile(r'(.*) \((\d{1,3})\)(.*)')

# 拡張子.jpgのファイルを取得する
path = './*.jpg'

# txtファイルを取得する
flist = glob.glob(path)
print('変更前')
print(flist)

for file in flist:
    #file_name = name_ptrn.search(file).group(0)
    #num = name_ptrn.search(file).group(2)
    new_file_name = name_ptrn.search(file).group(1)+'_'+name_ptrn.search(file).group(2).zfill(3)+name_ptrn.search(file).group(3)
    #print(file)
    #print(new_file_name)
    os.rename(file, new_file_name)

list = glob.glob(path)
print('変更後')
print(list)

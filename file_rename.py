import re, glob, os, sys

def main(dry_run=False):

    ### dry-run
    # 強制dry-runモード(手動切替)
    enforce_dryrun = False

    # 何らかの引数が与えられたらdry-runモード
    if len(sys.argv) > 1 or enforce_dryrun:
        print("run dry-run mode")
        dry_run = True

    ### パラメータ
    ### こちらの記載内容を基本的には変更する
    # 拡張子.jpgのファイルを取得する
    path = './*.jpg'

    # 名前一致パターン
    #name_ptrn = re.compile(r'(.*) \((\d{1,3})\)(.*)')
    name_ptrn = re.compile(r'(.*)(\d{1,3})(.*)')

    ### プログラム開始
    # 該当ファイルを取得する
    flist = glob.glob(path)
    print('変更前')
    print(flist)

    new_file_name_list = []

    for file in flist:
        #new_file_name = name_ptrn.search(file).group(1)+'_'+name_ptrn.search(file).group(2).zfill(3)+name_ptrn.search(file).group(3)
        new_file_name = name_ptrn.search(file).group(1)+name_ptrn.search(file).group(2).zfill(3)+name_ptrn.search(file).group(3)
        new_file_name_list.append(new_file_name)
        if not dry_run:
            os.rename(file, new_file_name)

    list = glob.glob(path)
    print('変更後')
    if dry_run:
        print(new_file_name_list)
    else:
        print(list)
    

if __name__ == "__main__":
    main()

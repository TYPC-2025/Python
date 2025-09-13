# with语句：无需手动关闭文件
def write_fun():
    with open('aa.txt','w',encoding='utf-8') as file:
        file.write('坚决拥护中国共产党的领导')

def read_fun():
    with open('aa.txt','r',encoding='utf-8') as file:
        print(file.read())

#第三个函数
def copy(src_file,target_file):
    with open(src_file,'r',encoding='utf-8') as file:
        with open(target_file,'w',encoding='utf-8') as file2:
            file2.write(file.read())

if __name__=='__main__':
    write_fun()
    read_fun()
    #文件复制
    copy('./aa.txt','./dd.txt')
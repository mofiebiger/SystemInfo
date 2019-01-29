'''
Created on Jan 24, 2019

@author: mo
'''
import platform

def main():
    print(platform.platform())
    print(platform.machine())
    print(platform.version())
    print(platform.system())
    print(platform.uname())
    print(platform.processor())

    return 

if __name__ == '__main__':
    main()
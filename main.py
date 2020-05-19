# main
import scanner
# import tkwindow

RUNNINGMODE = 'ctl'

if __name__ == '__main__':
    sc = scanner.Scanner()

    pass

    if RUNNINGMODE == 'ctl':
        ip = input('ip:')
        sctype = input('type:\n1.all\n2.general\nuse:')
        if sctype == '1':
            sctype = 'all'
        elif sctype == '2':
            sctype = 'general'
        else:
            exit(-2)
        sc.set_address(ip)
        sc.set_scantype(sctype)
        sc.start()
        sc.show_ports()
        exit(0)

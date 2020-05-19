# 全连接扫描器
import socket
import math


class Scanner(object):
    def __init__(self):
        self.ip_address = ''  # IP地址
        self.address = ''  # 地址信息
        self.port_init = 1  # 起始端口
        self.port_fini = 65535  # 终止端口
        self.scan_type = 'all'  # 扫描类型
        self.timeout = 0  # 超时次数
        self.open_port = list()  # 开放的端口
        self.total_type = ['all', 'general']  # 可选的扫描类型
        self.general_ports = range(1, 1000)  # 常用端口段

    def get_port(self):
        return self.open_port

    def set_address(self, ip_address):
        self.ip_address = ip_address
        return False

    def set_scantype(self, type_):
        if type_ in self.total_type:
            self.scan_type = type_
        else:
            raise ValueError(f'Scan type "{type_}" not found!')
        self.scan_type = type_
        return False

    def show_ports(self):
        print(f'ip {self.ip_address} open ports below:')
        for p in self.open_port:
            print(p, end='', sep='\t')
        return False

    def scan(self, ports):
        if type(ports) != int:
            raise TypeError('argument "ports" is %s expect int' % type(ports))
        scan_socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)
        self.address = self.ip_address, ports
        while True:
            try:
                scan_socket.connect(self.address)
            except ConnectionRefusedError:
                return False
            except ConnectionResetError:
                return False
            except ConnectionAbortedError:
                return False
            except TimeoutError:
                if self.timeout >= 4:
                    self.timeout = 0
                    return False
                self.timeout += 1
                continue
            break
        return True

    def start(self):
        print('Using type: ', self.scan_type)
        if self.open_port:
            self.open_port.clear()

        if self.scan_type == 'all':
            if 0 > self.port_init > self.port_fini > 65535:
                raise ValueError(f'Range of port invalid ! ( {self.port_init} - {self.port_fini} )')
            current_port = 1
            while True:
                if current_port >= self.port_fini:
                    break
                print('Now:{}'.format(current_port), '\r', end='')
                if self.scan(current_port):
                    self.open_port.append(current_port)
                current_port += 1
        elif self.scan_type == 'general':
            for current_port in self.general_ports:
                print('Now:{}'.format(current_port), '\r', end='')
                if self.scan(current_port):
                    self.open_port.append(current_port)
        else:
            raise ValueError(f'Scan type "{self.scan_type}" not found!')
        return False


if __name__ == '__main__':
    print('try to run main.py instead')
    exit(-10)

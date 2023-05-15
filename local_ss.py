import os
import socket
import struct
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


# Shadowsocks 服务器的配置信息
server_address = "147.182.204.108"  # 服务端地址
server_port = 8877  # 服务端端口
password = "xyzxyz"  # Shadowsocks 密码
method = "aes-256-cfb"  # Shadowsocks 加密方法

# 目标网站的配置信息
target_address = "example.com"
target_port = 80

# 初始化加密器
key = password.encode()[:32]
cipher = Cipher(algorithms.AES(key), modes.CFB8(key[:16]), backend=default_backend())
encryptor = cipher.encryptor()
decryptor = cipher.decryptor()

# 与 Shadowsocks 服务器建立连接
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_address, server_port))

# 构造 Socks5 请求头
address_type = 1  # IPv4 address
address = b"".join([struct.pack("!B", int(i)) for i in target_address.split(".")])
request_header = (
    struct.pack("!BBH", address_type, *struct.unpack("!H", socket.htons(target_port)))
    + address
)

# 使用 Shadowsocks 加密请求头

print(response[:100])  # 输出目标服务器的响应内容

sock.close()

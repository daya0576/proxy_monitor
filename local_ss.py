import os
import socket
import struct


# Shadowsocks 服务器的配置信息
server_address = "147.182.204.108"  # 服务端地址
server_port = 8877  # 服务端端口
password = "xyzxyz"  # Shadowsocks 密码
method = "aes-256-cfb"  # Shadowsocks 加密方法

# 目标网站的配置信息
target_address = "example.com"
target_port = 80

# ADSL 拨号服务器,搭建配置文件

* 购买云立方的vps服务器

系统：centos 7

1. 配置代理服务器：

```python
adsl-start    #启动
```
2.　安装squid和httpd

```python
yum install -y squid
yum install httpd-tools -y
yum install openssl
```

3.  修改配置文件

```python
vi /etc/squid/squid.conf
```
将里面的内容全部替换成下面的内容,直接复制替换掉就ok
[https://github.com/Derek520/ADSL/blob/master/squid.conf](https://github.com/Derek520/ADSL/blob/master/squid.conf)

4.　生成用户名和密码

```python
htpasswd -c /etc/squid/passwd testadsl       #创建一个密码文件名为passwd，账号名为airoot的密码文件
# 回车之后提示输入密码，在此这里我设置的密码为 321654
# 注意密码不要超过8位　
```

5. 检查参数

```python
squid -k parse
```

6. 初始化参数

```python
squid -z

2018/11/07 00:09:11| WARNING: (B) '127.0.0.1' is a subnetwork of (A) '127.0.0.1'
2018/11/07 00:09:11| WARNING: because of this '127.0.0.1' is ignored to keep splay tree searching predictable
2018/11/07 00:09:11| WARNING: You should probably remove '127.0.0.1' from the ACL named 'localhost'
2018/11/07 00:09:11| WARNING: (B) '127.0.0.1' is a subnetwork of (A) '127.0.0.1'
2018/11/07 00:09:11| WARNING: because of this '127.0.0.1' is ignored to keep splay tree searching predictable
2018/11/07 00:09:11| WARNING: You should probably remove '127.0.0.1' from the ACL named 'localhost'
2018/11/07 00:09:11| WARNING: (B) '::1' is a subnetwork of (A) '::1'
2018/11/07 00:09:11| WARNING: because of this '::1' is ignored to keep splay tree searching predictable
2018/11/07 00:09:11| WARNING: You should probably remove '::1' from the ACL named 'localhost'
2018/11/07 00:09:11| WARNING: (B) '::1' is a subnetwork of (A) '::1'
2018/11/07 00:09:11| WARNING: because of this '::1' is ignored to keep splay tree searching predictable
2018/11/07 00:09:11| WARNING: You should probably remove '::1' from the ACL named 'localhost'
2018/11/07 00:09:11| WARNING: (B) '127.0.0.0/8' is a subnetwork of (A) '127.0.0.0/8'
2018/11/07 00:09:11| WARNING: because of this '127.0.0.0/8' is ignored to keep splay tree searching predictable
2018/11/07 00:09:11| WARNING: You should probably remove '127.0.0.0/8' from the ACL named 'to_localhost'
2018/11/07 00:09:11| WARNING: (B) '0.0.0.0' is a subnetwork of (A) '0.0.0.0'
2018/11/07 00:09:11| WARNING: because of this '0.0.0.0' is ignored to keep splay tree searching predictable
2018/11/07 00:09:11| WARNING: You should probably remove '0.0.0.0' from the ACL named 'to_localhost'
2018/11/07 00:09:11| WARNING: (B) '0.0.0.0' is a subnetwork of (A) '0.0.0.0'
2018/11/07 00:09:11| WARNING: because of this '0.0.0.0' is ignored to keep splay tree searching predictable
2018/11/07 00:09:11| WARNING: You should probably remove '0.0.0.0' from the ACL named 'to_localhost'
2018/11/07 00:09:11| WARNING: (B) '::1' is a subnetwork of (A) '::1'
2018/11/07 00:09:11| WARNING: because of this '::1' is ignored to keep splay tree searching predictable
2018/11/07 00:09:11| WARNING: You should probably remove '::1' from the ACL named 'to_localhost'
2018/11/07 00:09:11| WARNING: (B) '::1' is a subnetwork of (A) '::1'
2018/11/07 00:09:11| WARNING: because of this '::1' is ignored to keep splay tree searching predictable
2018/11/07 00:09:11| WARNING: You should probably remove '::1' from the ACL named 'to_localhost'
[root@localhost ~]# 2018/11/07 00:09:12 kid1| WARNING: (B) '127.0.0.1' is a subnetwork of (A) '127.0.0.1'
2018/11/07 00:09:12 kid1| WARNING: because of this '127.0.0.1' is ignored to keep splay tree searching predictable
2018/11/07 00:09:12 kid1| WARNING: You should probably remove '127.0.0.1' from the ACL named 'localhost'
2018/11/07 00:09:12 kid1| WARNING: (B) '127.0.0.1' is a subnetwork of (A) '127.0.0.1'
2018/11/07 00:09:12 kid1| WARNING: because of this '127.0.0.1' is ignored to keep splay tree searching predictable
2018/11/07 00:09:12 kid1| WARNING: You should probably remove '127.0.0.1' from the ACL named 'localhost'
2018/11/07 00:09:12 kid1| WARNING: (B) '::1' is a subnetwork of (A) '::1'
2018/11/07 00:09:12 kid1| WARNING: because of this '::1' is ignored to keep splay tree searching predictable
2018/11/07 00:09:12 kid1| WARNING: You should probably remove '::1' from the ACL named 'localhost'
2018/11/07 00:09:12 kid1| WARNING: (B) '::1' is a subnetwork of (A) '::1'
2018/11/07 00:09:12 kid1| WARNING: because of this '::1' is ignored to keep splay tree searching predictable
2018/11/07 00:09:12 kid1| WARNING: You should probably remove '::1' from the ACL named 'localhost'
2018/11/07 00:09:12 kid1| WARNING: (B) '127.0.0.0/8' is a subnetwork of (A) '127.0.0.0/8'
2018/11/07 00:09:12 kid1| WARNING: because of this '127.0.0.0/8' is ignored to keep splay tree searching predictable
2018/11/07 00:09:12 kid1| WARNING: You should probably remove '127.0.0.0/8' from the ACL named 'to_localhost'
2018/11/07 00:09:12 kid1| WARNING: (B) '0.0.0.0' is a subnetwork of (A) '0.0.0.0'
2018/11/07 00:09:12 kid1| WARNING: because of this '0.0.0.0' is ignored to keep splay tree searching predictable
2018/11/07 00:09:12 kid1| WARNING: You should probably remove '0.0.0.0' from the ACL named 'to_localhost'
2018/11/07 00:09:12 kid1| WARNING: (B) '0.0.0.0' is a subnetwork of (A) '0.0.0.0'
2018/11/07 00:09:12 kid1| WARNING: because of this '0.0.0.0' is ignored to keep splay tree searching predictable
2018/11/07 00:09:12 kid1| WARNING: You should probably remove '0.0.0.0' from the ACL named 'to_localhost'
2018/11/07 00:09:12 kid1| WARNING: (B) '::1' is a subnetwork of (A) '::1'
2018/11/07 00:09:12 kid1| WARNING: because of this '::1' is ignored to keep splay tree searching predictable
2018/11/07 00:09:12 kid1| WARNING: You should probably remove '::1' from the ACL named 'to_localhost'
2018/11/07 00:09:12 kid1| WARNING: (B) '::1' is a subnetwork of (A) '::1'
2018/11/07 00:09:12 kid1| WARNING: because of this '::1' is ignored to keep splay tree searching predictable
2018/11/07 00:09:12 kid1| WARNING: You should probably remove '::1' from the ACL named 'to_localhost'
2018/11/07 00:09:12 kid1| Set Current Directory to /var/spool/squid
2018/11/07 00:09:12 kid1| Creating missing swap directories
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/00
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/01
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/02
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/03
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/04
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/05
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/06
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/07
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/08
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/09
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/0A
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/0B
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/0C
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/0D
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/0E
2018/11/07 00:09:12 kid1| Making directories in /tmp/squid/0F
```
* 以上就是初始化成功了，会卡在那里，直接ctrl+c退出就可以

6. 启动服务

```python
 # 启动
systemctl start squid.service
# 停止
systemctl stop squid.service
# 重启
systemctl restart squid.service
```
启动若报错,提示：Redirecting to /bin/systemctl restart  squid.service

```python
/bin/systemctl restart  squid.service
```

7. 测试搭建的代理服务器

```python
ifconfig
网卡：ppp0 ip　xxx.xxx.xxx.xxx
curl -x xxx.xxx.xxx.xxx:3828 -U airoot:123456 www.baidu.com
```


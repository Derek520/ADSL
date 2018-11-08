# ADSL 拨号服务器,搭建配置文件

### squid
* 购买云立方的vps服务器

* 系统：centos 7

1. 配置代理服务器：

```python
adsl-start    #启动
```
2. 安装squid和httpd

```python
yum install -y squid
yum install httpd-tools -y
yum install openssl
```

3. 修改配置文件

```python
vi /etc/squid/squid.conf
```
将里面的内容全部替换成下面的内容,直接复制替换掉就ok  

[https://github.com/Derek520/ADSL/blob/master/squid.conf](https://github.com/Derek520/ADSL/blob/master/squid.conf)

4. 生成用户名和密码

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
网卡：ppp0 ip　xxx.xxx.xxx.xxx airoot:123456是第四步生成的用户和密码
curl -x xxx.xxx.xxx.xxx:3828 -U airoot:123456 www.baidu.com
```

### 第二种：TinyProxy

1. 这个很简单，直接安装

```python
yum install -y epel-release
yum update -y
yum install -y tinyproxy
```

2. 配置TinyProxy

```python
vim /etc/tinyproxy/tinyproxy.conf

#端口
Port 8888
#　注释掉是允许所有ip访问  
#Allow 127.0.0.1 
# 注释掉下面这行，隐藏掉Via请求头部
DisableViaHeader Yes
```

3. 更多配置项，下面是列举一些配置文件默认的，不需要配置：

```python
PidFile "/var/run/tinyproxy/tinyproxy.pid"
LogFile "/var/log/tinyproxy/tinyproxy.log"
LogLevel Info
MaxClients 100
MinSpareServers 5
MaxSpareServers 20
StartServers 10
```

4. 命令，启动即可:

```python
systemctl start tinyproxy.service 
systemctl restart tinyproxy.service 
systemctl stop tinyproxy.service 
systemctl status tinyproxy.service 
systemctl enable tinyproxy.service 
```

5. 测试

```python
curl -x xxx.xxx.xxx.xxx:3828 www.baidu.com
```

### 事件驱动接口
> 网上好多都是给adsl服务器,做个定时任务,定时拨号,将新ip存入远端redis;个人不喜欢这种方式,我写的事件驱动,发送请求过去后,再拨号；

设计:  
    用flask写个接口,使用python2,不要问为什么不用python3,实在是服务器太小,只写个接口接收请求,既然自带了python2,就懒得换了;  
    当ip被封时,需要删除该ip获取新的ip；使用被封的ip发送get请求，adsl服务器收到请求后，删除对应服务器ip,并停止接口;因为一旦重新拨号,该接口就失效，需要重启该接口;　　
    创建shell脚本,进行死循环监控api接口,是否在运行,若是停止运行,说明接口收到拨号请求;重新拨号,将获取到的ip,存进远端redis数据库,再重启api接口,等待下一次请求；　　
    
1. 只需要安装　api.txt中包,就可以

```python
pip install -r api.txt  #如果没有pip　需要安装pip
```

2. 将clinet文件下载,放在adsl服务器上:

- 需要修改配置文件中的redis信息,

```python
NETWORK = 'ppp0'    # 拨号后网卡名字
REDIS_HOST = ""
REDIS_PORT = 6380
REDIS_DB = 11
REDIS_PASSWORD = ''

# hash存储
KEY = 'proxies'
FIELD = 'a1'
```

```python
# 进入目录
cd  clinet
#　保证文件可执行 
chmod +x process.sh
# 进行后台运行,运行时，需要保证后台没有process在运行，如果有kill掉，再启动
nohup ./process.sh >process.log 2>&1 &
# 查看实时输出log
tail -f process.log
```
3. 查看自己配置的redis库中是否有ip

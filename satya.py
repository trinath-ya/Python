#!/usr/bin/python
import os
import subprocess
import paramiko
import datetime
#import Mysqldb
import pymysql as MySQLdb
now = datetime.datetime.now()
t=now.strftime("%Y-%m-%d %H:%M")
f=open("tlgcdb_apiips.txt","r")
data=f.readlines()
key_path="/home/ec2-user/.ssh/.tlgcdb-ore-prd-key.pem"
username="ec2-user"
com="free"

def fun(key_path,ip):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    privkey = paramiko.RSAKey.from_private_key_file(key_path)
    ssh.connect(ip,username='ec2-user',pkey=privkey)
    stdin, stdout, stderr = ssh.exec_command('free')
    stdin.flush()
    m=stdout.read()
    s=m.split()
    mem=s[8]
    return mem


for row in data[1:]:
    ip= row.strip()
    m=fun(key_path,ip)
    print "Time:%s , Region:US , IPAddress:%s , Memory:%s"%(t,ip,m)
    #conn=MySQLdb.connect(host='localhost',user='root',passwd='tlg$123')
    conn=MySQLdb.connect("localhost","root","tlg$123")
    cursor = conn.cursor()
    q="insert into customer values(%s, 'US', %s, %s)"%(t,ip,m)
    cur.execute(q)
    conn.commit()
    conn.close()

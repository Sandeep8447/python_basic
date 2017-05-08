#_*_coding:utf-8_*_
__author__ = 'jieli'
import commands
import os
import sys

from conf import settings
from modules import demo

import multi_task
import mysql_conn


def call(sys_args):

    if len(sys_args) == 0:
        feature_list()
    else:
        feature_ins = Features()
        if hasattr(feature_ins, sys_args[0]):
            func = getattr(feature_ins,sys_args[0])
            func(sys_args)
        else:
            print "\033[31;1mInvalid argument!\033[0m"
            feature_list()
def feature_list():
    features = '''
    run     run audit interactive interface
    init    create audit database tables
            --with_sample_data create audit database tables with sample data
    manage  management interface for administrator
    help    show helps
    '''
    print(features)
class Features(object):

    def __init__(self):
        pass

    def run(self,argv):
        self.ms = mysql_conn.MysqlConn()
        #print '-->res:',ms.insert("insert into user(username,password) values(%s,%s)" , ('rain','rain123'))
        if  self.__auth(self.ms):

            print(settings.Welcome_msg)
            self.__user_interactive()
    def __user_interactive(self):
        self.fetch_hosts()
    def __auth(self,mysql_conn):
       import getpass
       count = 0
       while count < 3:
            user = raw_input("Username:").strip()
            passwd = getpass.getpass("Password:")
            if len(user) == 0 or len(passwd) == 0:
                print "Username or password cannot be empty!"
                continue
            user_in_db  = mysql_conn.select("select * from user where username=%s and password=%s",(user,passwd))
            if len(user_in_db) > 0: #pass authentication
                self.login_user = user
                self.user_id = user_in_db[0][2]

                return True
            else:
                print "\033[31;1mInvalid username or password!\033[0m"
                count +=1
       else:
           sys.exit("Invalid username and password, too many attempts,exit.")
    def fetch_hosts(self):
        host_id_list_query = '''
          SELECT host_groups.id ,
              host_groups.group_id ,
              host_groups.user_id,
              bind_hosts.host_id,
              bind_hosts.host_user_id
          from host_groups,bind_hosts
          where host_groups.user_id =%s and host_groups.bind_host_id = bind_hosts.id '''
        host_id_list = self.ms.select(host_id_list_query,(self.user_id,))
        host_list = {}
        for i in host_id_list:
            if not host_list.has_key(i[1]): #i[1] = group_id
                group_name = self.ms.select("select name from groups where id=%s", (i[1],))[0][0]

                host_list[i[1]]= {
                    'node' : [],
                    'name' : group_name
                }
            host_user_info = self.ms.select("select username,password from host_users where id=%s ", (i[4],))[0]
            host_info = self.ms.select("select hostname,ip from hosts where id=%s ", (i[3],))[0]

            host_info_dic = {
                'id': None ,
                'hostname':host_info[0],
                'ip':host_info[1],
                'username': host_user_info[0],
                'password': host_user_info[1],
                'port': 22,
            }


            host_list[i[1]]['node'].append(host_info_dic)
        exit_flag = False
        while not exit_flag:
            try:
                print '------- Available Groups -------'
                for index,key in enumerate(host_list):
                    print '%s.  %s  [%s]' %(index,host_list[key]['name'],len(host_list[key]['node']))

                print "--------------------------------"
                print "[Enter m to multiple task mode]"
                user_choice = raw_input("\033[32;1m>>>:\033[0m").strip()
                if len(user_choice) == 0:continue
                if user_choice.isdigit():

                    user_choice = int(user_choice)
                    if user_choice <= len(host_list.keys()): #not exceeds the index range
                        choice_key = host_list.keys()[user_choice]
                        while not exit_flag:
                            for index2,host in enumerate(host_list[choice_key]['node']):
                                print '\t%s. %s(%s) \tuser:%s' %(index2,host['hostname'],host['ip'],host['username'])
                            user_choice2 = raw_input("\033[32;1m>>>:\033[0m").strip()
                            h_list = host_list[choice_key]['node']
                            if len(user_choice2) == 0:continue
                            if user_choice2.isdigit():
                                user_choice2 = int(user_choice2)
                                if user_choice2 < len(h_list):

                                    #login('192.168.2.250', 22,'alex','alex3714')
                                    print '\033[32;1m-----connecting [%s] with user [%s]-----\033[0m' %(h_list[user_choice2]['ip'],h_list[user_choice2]['username'])
                                    try:
                                        demo.login(self,h_list[user_choice2]['ip'],
                                                   h_list[user_choice2]['port'],
                                                   h_list[user_choice2]['username'],
                                                   h_list[user_choice2]['password'])
                                    except Exception,e:
                                        print "\033[31;1m%s\033[0m" %e
                                else:
                                    print "\033[31;1mDoes not have this option [%s]\033[0m" % user_choice2


                    else:
                        print "\033[31;1mDoes not have this option [%s]\033[0m" % user_choice

                else:
                    if user_choice == 'm': #run multi_task
                            m= multi_task.MultiTask(self)
                            m.interactive()
                    if user_choice == 'exit':
                        sys.exit("Bye!")
            except (KeyboardInterrupt,EOFError):
                print "\033[31;1mEnter exit to logout\033[0m"
    def flush_audit_log(self,log_list):
        query_code = '''insert into audit_log (user,ip,host_user,cmd,date) values(%s,%s,%s,%s,%s) '''
        execute_status = self.ms.insert_many(query_code,log_list)
        if execute_status:
            return True
    def handle_cmd(self,cmd):
        print '------>',cmd
    def init(self,msg):
        '''create database tables'''
        print '-->',msg
        base_dir ='/'.join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])
        db_file = '%s/%s' %(base_dir,settings.DatabaseInitSqlFile)
        if '--with_sample_data' in msg:
            db_file = '%s/%s' %(base_dir,settings.DatabaseInitSqlFileWithSample)

        restore_cmd = "mysql -u%s -p%s -h%s %s <%s" %(settings.DATABASE['username'],
                                                      settings.DATABASE['password'],
                                                      settings.DATABASE['host'],
                                                      settings.DATABASE['db_name'],
                                                      db_file
                                                      )

        exec_res = commands.getstatusoutput(restore_cmd)

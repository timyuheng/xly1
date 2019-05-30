"""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
"""

# 标准模块
import sys
import json
import datetime
from prettytable import PrettyTable

# 定义变量
RESULT = {}
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("51reboot", "123456")
FILENAME = "51reboot.txt"
FIELDS = ("name", "age", "tel", "email")


while INIT_FAIL_CNT < MAX_FAIL_CNT:

    username = input("Please input your username: ")
    password = input("Please input your password: ")

    if username == USERINFO[0] and password == USERINFO[1]:

        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        while True:
            # 业务逻辑

            # add monkey 12 132xxx monkey@51reboot.com
            info = input("Please input your operation: ").strip()  # 去前后空格
            info_list = info.split()
            if len(info) == 0: # 如果为空， 则提示
                print("Input info invalid, Please input again.")
                continue
            action = info_list[0]
            if action == "add":
                if len(info_list) == 4:
                    print("Add info invalid, Please add again.")
                    continue

                # 判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
                username = info_list[1]
                if username in RESULT:
                    print("Username {} already exists.".format(username))
                    continue
                else:
                    RESULT[username] = dict(zip(FIELDS, info_list[1:]))
                    print(RESULT)
                    print("Add {} succ.".format(username))

            elif action == "delete":
                # delete monkey1
                username = info_list[1]
                isSucc = RESULT.pop(username, None)
                if isSucc == None:
                    print("User {} not found.".format(username))
                else:
                    print("User {} Delete succ.".format(username))

            elif action == "update":
                # update monkey1 set age = 20

                username = info_list[1]
                where = info_list[2]
                fuhao = info_list[-2]

                if where != "set" or fuhao != "=":
                    print("Update method error.")
                    break

                NAMES = []

                for i in RESULT:
                    name = i[0]
                    NAMES.append(name)

                if username in NAMES:
                    idx = NAMES.index(username)
                    if info_list[3] == "age":
                        RESULT[idx][1] = info_list[-1]
                    elif info_list[3] == "tel":
                        RESULT[idx][2] = info_list[-1]
                    elif info_list[3] == "email":
                        RESULT[idx][3] = info_list[-1]
                else:
                    print("User {} not found.".format(username))

            elif action == "list":
                # 如果没有一条记录， 那么提示为空
                if len(RESULT) == 0 :
                    print("not data.")
                    continue

                xtb = PrettyTable()
                xtb.field_names = FIELDS
                for k, v in RESULT.items():
                    xtb.add_row(v.values())
                print(xtb)

            elif action == "find":
                # 查找
                username = info_list[1]
                userinfo = RESULT.get(username, None)
                if userinfo == None:
                    print("Username {} not found.".format(username))
                else:
                    xtb = PrettyTable()
                    xtb.field_names = FIELDS
                    xtb.add_row(userinfo.values())
                    print(xtb)

            elif action == "save":
                # save
                # 1. 打开文件 file describe
                fd = open(FILENAME, 'w')

                # 2. 操作文件 read / write
                fd.write(json.dumps(RESULT))

                # 3. 关闭文件
                fd.close()

                print("Save file:{} succ.".format(FILENAME))

            elif action == "load":
                # load

                # 1. 打开文件 file describe
                fd = open(FILENAME, 'r')

                # 2. 操作文件 read / write
                data = fd.read()
                RESULT = json.loads(data)

                # 3. 关闭文件
                fd.close()
                print("Load file:{} succ.".format(FILENAME))

            elif action == "display":
                # dispaly page 2 pagesize 5
                # default = 5
                if len(info_list[1:]) >= 2 and len(info_list[1:]) <= 4:

                    pagesize = 5
                    if len(info_list[1:]) == 2:
                        if info_list[1] == "page":
                            pagesize = 5
                        else:
                            print("Display info invalid. Please input again.")
                            continue

                    else:
                        if info_list[1] == "page" and info_list[3] == "pagesize":
                            pagesize = int(info_list[-1])
                        else:
                            print("Display info invalid. Please input again.")
                            continue

                    page = int(info_list[2]) - 1
                    data = []
                    for k, v in RESULT.items():
                        data.append(v.values())

                    # start, end sep
                    start = page * pagesize
                    end = start + pagesize
                    print("Start: {}, End:{}".format(start, end))

                    xtb = PrettyTable()
                    xtb.field_names = FIELDS
                    for userinfo in data[start:end]:
                        xtb.add_row(userinfo)
                    print(xtb)
                else:
                    print("Input info invalid, Please input again.")
                    continue

            elif action == "exit":
                sys.exit(0)
            else:
                print("invalid action.")
    else:
        # 带颜色
        print("username or password error.")
        INIT_FAIL_CNT += 1

print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))

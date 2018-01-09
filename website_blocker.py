import time
import datetime
import sys


hosts_path = r'C:/Windows/System32/drivers/etc/hosts'
redirect = '127.0.0.1'
website_list = ['facebook.com', 'quora.com', 'chess.com']
hosts_temp = 'hosts_temp'
blocked = False
start_time = datetime.datetime.now()

user_inputs = sys.argv[1:]

def add_www(lst):
    '''takes in list of websites and adds 'www.' to them'''
    new_lst = []
    for website in lst:
        new_lst.append(website)
        new_lst.append('www.' + website)
    return new_lst

def add_blocks(website_list, hosts_path):
    '''add to-block sites to hosts'''
    print('Working hours...')
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write('\n' + redirect + '  ' + website)
    return None

def remove_blocks(website_list, hosts_path):
    '''remove blocked sites from hosts'''
    print('fun hours...')
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()
    return None

def condition(now, inputs = user_inputs):
    '''return True if the websites should be blocked right now, and False otherwise.'''
    if len(inputs) > 0:
        return timer(start_time, now, get_seconds(inputs))
    elif datetime.datetime(now.year, now.month, now.day, 10) < now < datetime.datetime(now.year, now.month, now.day, 18):
        return True
    return False

def get_seconds(inputs):
    if type(inputs) == int or type(inputs) == str or type(inputs) == float:
        return int(float(inputs) * 60)
    elif type(inputs) == list:
        try:
            int(inputs[0])
        except:
            raise Exception('cannot parse how long you want websites to be blocked!')
    else:
        raise Exception('cannot parse how long you want websites to be blocked!') 
    if len(inputs) == 1:
        return int(float(inputs[0]) * 60)
    elif len(inputs) == 2:
        if inputs[1][0].lower() == 's':
            return int(inputs[0])
        elif inputs[1][0].lower() == 'm':
            return int(float(inputs[0]) * 60)
        elif inputs[1][0].lower() == 'h':
            return int(float(inputs[0]) * 3600)
    else:
        raise Exception('cannot parse how long you want websites to be blocked!')
    
def timer(start, end, difference):
    '''
    start: datetime.datetime object
    end: datetime.datetime object
    difference: integer
    returns True if end - start < difference
    '''
    if end - start < datetime.timedelta(seconds = difference):
        return True
    return False
        
    
website_list = add_www(website_list)

while True:
    now = datetime.datetime.now()
    if condition(now) and not blocked:
        add_blocks(website_list, hosts_path)
        blocked = True
    elif not condition(now) and blocked:
        remove_blocks(website_list, hosts_path)
        blocked = False
    time.sleep(10)
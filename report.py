import os
import re

files_in_dir = []
for r, d, f in os.walk('./report/'):
    for item in f:
        if '.txt' in item:
            files_in_dir.append(os.path.join(r, item))

total_data = 0
for item in files_in_dir:
    with open(item, 'r') as file:
        data = file.read()
        x = re.search('Cumulative.+', data)
        if(x is None):
            print('Cumulative not found in:\n', data)
        else:
            s = x.group(0)
            total = re.search('(\d+\.)?\d+(KB|MB)$', s)
            if(total is None):
                print('Total not found in:\n', s)
            else:
                d = total.group(0)
                if('KB' in d):
                    total_data += float(d.replace('KB', '')) / 1024
                elif('MB' in d):
                    total_data += float(d.replace('MB', ''))
                else:
                    print('Undefined data unit')

print('Total YouTube data usage: ', "%.2f" % total_data, ' MB')

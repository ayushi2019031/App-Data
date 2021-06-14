import json
from re import sub

import matplotlib.pyplot as plt
def fun(file_name):
    f = open(file_name, encoding='utf-8');

    dictionary_list = []

    json_text = sub(',\s+\]', ']', f.read()) # We need to repair the data
    dictionary_list.extend(json.loads(json_text))

    # print(dictionary_list);

    developer_info = {}

    for k in dictionary_list:
        if (not (k['developer'] in developer_info)):
            developer_info[k['developer']] = 0; 
        developer_info[k['developer']] = developer_info.get(k['developer']) + 1;

    developers = list(developer_info.keys())
    frequencies =list(developer_info.values());
 
    plt.bar(developers, frequencies, color ='maroon',width = 0.4)
    plt.show();
    print(len(dictionary_list));
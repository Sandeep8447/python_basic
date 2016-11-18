dict = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
dict.clear()

menu = {
    'Beijing': {
        "ChaoYang": {
            "CBD": ['CICC', 'CCTV'],
            "JinRongJie": [""],
            "WangJing": ["Momo","Stamp"]
        },
        "HaiDian": ['Baidu', 'Youku']
    },

    'Shanghai': {
        "PuDong": ['Ctrip', '1 Shop'],
        "PuXi": ['China Bank', 'Amerian Bank']
    }
}

print menu["Beijing"]["ChaoYang"]["WangJing"][0]
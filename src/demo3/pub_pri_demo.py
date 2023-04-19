# 访问权限
def _huangjin_vip(lv):
    print('尊敬的黄金会员，你好')
    vip_name =  '黄金会员' + str(lv)
    return vip_name
def _gold_vip(lv):
    print('尊敬的大众会员，你好')
    vip_name =  '大众会员' + str(lv)
    return  vip_name
def vip_lv_name(lv):
    if lv == 1:
        print(_gold_vip(lv))
    elif lv == 2:
        print(_huangjin_vip(lv))
vip_lv_name(2)


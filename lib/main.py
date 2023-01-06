from investments.investment import Investment

inv = Investment(fp = r'C:\dev\fundreport\templates\traditional_gic.json')
inv_obj = inv.instance
print(inv_obj)
import re
pattern='[?|&|=]'
s2='o7AS?spm_id_from=333.788.player.switch&vd_source='
lst=re.split(pattern,s2)
print(lst)
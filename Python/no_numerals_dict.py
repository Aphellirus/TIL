# In scientific and technical writing, the prevailing style is to write out numbers under ten. 
# This dictionary will spell out all numerals under 10.
dict = {'0' : 'zero',
'1':'one',
'2': 'two',
'3': 'three',
'4':'four',
'5':'five',
'6':'six',
'7':'seven',
'8':'eight',
'9':'nine',
'10':'ten'
}
i = input()
s = "0123456789"
if "10" in i:
    i = i.replace("10", dict['10'])

for ch in s:
    if ch == '0':
        i = i.replace(ch, dict['0'])
    if ch == '1':
        i = i.replace(ch, dict['1'])
    if ch == '2':
        i = i.replace(ch, dict['2'])        
    if ch == '3':
        i = i.replace(ch, dict['3'])
    if ch == '4':
        i = i.replace(ch, dict['4'])
    if ch == '5':
        i = i.replace(ch, dict['5'])
    if ch == '6':
        i = i.replace(ch, dict['6'])
    if ch == '7':
        i = i.replace(ch, dict['7'])
    if ch == '8':
        i = i.replace(ch, dict['8'])
    if ch == '9':
        i = i.replace(ch, dict['9'])
print (i)

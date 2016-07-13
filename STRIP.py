# strip() mainly reduces the whitespace,tab,newline
# lstrip() and rstrip() remove whitespace characters from the left and right ends

spam = '      Hello World   '
print spam.strip()
print spam.lstrip()
print spam.rstrip()

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print spam.strip('ampS')

name = 'iftekharul islam'
print name.strip('is')

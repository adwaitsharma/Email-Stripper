import re

irritating=re.compile('\n[s|S]ent (via|from) .*\n')

email='''Dear foo,
foo bar foobar
foo foo bar bar

sent via Blackberry
-- 
Regards,
Adwait Sharma'''

print "String-\n",email
print "\n***Running regex***\n"
email=irritating.sub('\n',email)
print email

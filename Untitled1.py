# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>



# <codecell>

s = "1234abcd5678efgh"
[s[i:i+4] for i in range(len(s))][-4::-4]

#12345678901234567890123456789012345678901234567890
n=len(s)
print ((s*(n/4)+'    ')*4)
print ((s*(n/4)+' '*8)*4)[12::n+1]

# <codecell>

a = "efgh5678abcd1234"
print s == a

# <codecell>

s = "1234abcd5678efgh"
n=len(s);s=((s*4+' '*8)*(n/4))[n-4:-4:n+1]
#2345678901234567890123456789012345678901234567890
s

# <codecell>

s = "1234abcd5678efgh"

# <codecell>

a

# <codecell>


# <codecell>



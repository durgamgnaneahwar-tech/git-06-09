
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 

rows=5
for row in range(1,rows+1):
    res=""
    for col in range(1,row+1):
        res+=str(row)+" "
    print(res)



rows=15
for rows in range(rows,0,-1):
    res=""
    for col in range(1,rows+1):
        res+="% "
    print(res) 

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

rows=5
for rows in range(rows,0,-1):
    res=""
    for col in range(1,rows+1):
        res+="* "
    print(res)


# @ @ @ @ @ 
# @       @ 
# @       @ 
# @       @ 
# @ @ @ @ @ 


rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or j==rows or j==1 or j==rows:
            res+="@ "
        else:
            res+=" "+" "
    print(res)


# $       $ 
#   $   $   
#     $     
#   $   $   
# $       $ 

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==j or i+j==rows+1:
            res+="$ "
        else:
            res+="  "
    print(res)

# $ $ $ $ $ 
# $ $   $ $ 
# $   $   $ 
# $ $   $ $ 
# $ $ $ $ $ 

rows=20
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==j or i+j==rows+1 or i==rows or j==rows or i==1 or j==1:
            res+="* "
        else:
            res+="  "
    print(res)


# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,i+1):
        res+= str(j)+" "
    print(res)


rows=10
for i in range(1,rows+1):
    res=""
    for sp in range (1,(rows-i)+1):  #5-1+1   5-2+1
        res+=" "
    for j in range(1,i+1):
        res+="* "
    print(res)

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==3 or i==5 or j==1:
            res+="& "
        else:
            res+=" "
    print(res)

# +       + 
# +       + 
# + + + + + 
# +       + 
# +       + 


rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows or i==(rows//2)+1:
            res+="+ "
        else:
            res+=" "+" "
    print(res)
    
# + + + + + 
#     +     
#     +     
#     +     
# + + + + + 

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or j==(rows//2)+1:
            res+="+ "
        else:
            res+=" "+" "
    print(res)

# %       % 
# % %     % 
# %   %   % 
# %     % % 
# %       %


rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows or i==j:
            res+="% "
        else:
            res+=" "+" "
    print(res)

# % % % % % 
#       %   
#     %     
#   %       
# % % % % % 

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows+1 or i+j==rows+1 or i==5:
            res+="% "
        else:
            res+=" "+" "
    print(res)

# & & & & & 
# &         
# & & & & & 
#         &
# & & & & & 

rows=5
mid=rows//2 +1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i ==mid or i==rows or (j==1 and i<mid) or(i>mid and j==rows):
            res+="& "
        else:
            res+="  "
    print(res)


rows=5
for i in range(1,rows+1):
    res=" "
    for j in range(1,rows+1):
        if (i==1 or i==3 or i==5 or j==1 or i==5):
            res+=" *"
        if (j==rows and i<5):
            res+=""
    print(res)

#   * * * * *
#   *
#   * * * * *
#   *
#   * * * * *

#     *
#    ***
#   *****
#  *******
# *********

# 1 
# 2 4 
# 3 6 9 
# 4 8 12 16 
# 5 10 15 20 25 

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,i+1):
        res+= str(i*j)+" "
    print(res)


rows=7
for i in range(1,rows+1):
    res=""
    for sp in range(1,(rows-i)+1):
        res+=" "
    for j in range(1,i+1):
        res+="& "
    print(res)

for i in range(rows,0,-1):
    res=""
    for sp in range(1,(rows-i)+1):
        res+=" "
    for j in range(i+1,1):
        res+="& "
    print(res)




# Pyramid Pattern in Python
#  & & & & 
#   & & & 
#    & & 
#     & 
#     & 
#    & & 
#   & & & 
#  & & & & 
# & & & & & 

rows=5
for i in range(rows-1,0,-1):
    res=""
    for sp in range(1,(rows-i)+1):
        res+=" "
    for j in range(1,i+1):
        res+="& "
    print(res)

for i in range(1,rows+1):
    res=""
    for sp in range(1,(rows-i)+1):
        res+=" "
    for j in range(1,i+1):
        res+="& "
    print(res)


rows=5
for i in range(rows-1,0,-1):
    res=""
    for sp in range(1,(rows-i)+1):
        res+=" "
    for j in range(1,i+1):
        res+="% "
    print(res)


# X O X O X 
# O X O X O 
# X O X O X 
# O X O X O 
# X O X O X 

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if (i+j) %2==0:
            res+="X "
        else:
            res+="O "
    print(res)


# 2 3 
# 4 5 6 
# 7 8 9 10 

rows=4
n=1
for i in range(1,rows+1):
    res=""
    for j in range(1,i+1):
        res+= str(n) +" "
        n+=1
    print(res)






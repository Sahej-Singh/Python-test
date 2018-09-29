#icpc 2018 q1
m,n = int(input("")),int(input("")) 
k = int(input("enter k"))
a_list = []
b_list = []
s_list = []
t_list = []
p_list = []
for i in range(1,m+1):
	a,b,s,t = int(input("")),int(input("")),int(input("")),int(input(""))
	p = float(input(""))
	a_list.append(a)
	b_list.append(b)
	s_list.append(s)
	t_list.append(t)
	p_list.append(p)
print(m,n,k,a_list[0],a_list[1])
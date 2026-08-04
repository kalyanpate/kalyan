#Test file

# def add2(a,b):
#     return a+b

# ans =add2(5,3)
# print(ans)

# def sqare(a):
#     return a**2

# ans= sqare(40)
# print(ans)

# def even_odd(a):
#     ans = a%2
#     if ans==0:
#         return "even"
#     else:
#         return "odd"
# print(even_odd(5))

# def print_num(n):
#     for i in range(1,n):
#         print(i,end=" ")
# # print_num(5)

# sum_var = lambda a,b,c: a+b+c
# print(sum_var(1,2,3))
# x=10
# def ctss():
#     global x
#     x=x+8
# ctss()  
# print(x)

# 


# records = [	{"name":"Ravi","scores":[80,75,90]}, 	{"name":"Priya","scores":[45,50,30]}, 
# 	{"name":"Arjun","scores":[85,85,85]}, 	{"name":"Nisha","scores":[20,30,25]}]
# records =[{"name":"Sara","scores":[90,80]}, {"name":"Kabir","scores":[85,85]}]
# records =[{"name":"Aditi","scores":[]}, {"name":"Bharat","scores":[60,65,70]}]
# records =[]
# records=[{"name":"Rhea","scores":[20,25,15]}, {"name":"Tara","scores":[35,30,20]}, {"name":"Veer","scores":[]}]

# def summarize_cohart(records):
#     # print(records)
    
#     count =len(records) 
#     top_scorer = None    
#     above_threshold=()
#     failing=[]

#     hi_avg=0
#     names=[]
#     for rec in records:
#         # print(rec)
#         print(rec["scores"])
#         score=rec["scores"]
#         # print(len(score))
#         avg=0
#         for s in score:
#             avg +=s
#         if len(score) == 0:
#              avg = 0
#         else:
#             avg = avg / len(score)
       

#         # print(avg )
#         # print(rec["name"])
#         if avg > hi_avg:
#             hi_avg=avg
#             top_scorer=rec["name"]

#         # -----------------------------------       
#         if avg > 70:
#             names.append(rec["name"])
#         # print(names)
#         above_threshold = tuple(names)
#         # -------------------------------------
#         if avg < 40:
#             failing.append(rec["name"])
#         # print(failing)    


#     # print(count)
#     # print(top_scorer)
#     # print(above_threshold)
#     # print(failing)
#     dict_return= {"count": count, "top_scorer": top_scorer, "above_threshold" : above_threshold, "failing" : failing}
#     return dict_return


 
# print(summarize_cohart(records))

ls=[55,60,32,90,78,100]
print(ls[2:2])

for i in range(5):
    print(i)
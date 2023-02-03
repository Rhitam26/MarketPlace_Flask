# import bcrypt
# from pymongo import MongoClient
# from flask_bcrypt import bcrypt

# mongo = MongoClient('mongodb+srv://rhitamdeb26:margherita26@cluster0.uokqy8w.mongodb.net/?retryWrites=true&w=majority')


# # "********************************  Getting Data out of MongoDb **************************"
# # db = mongo["items"]
# # collection = db["items"]
# # dictItems=collection.find()
# # items=[]
# # for i in dictItems:
# #     i['id']= str(i['_id'])
# #     i.pop('_id')
# #     print(i)
# #     items.append(i)

# # print(items)



# db = mongo["DbUsers"]
# collection= db['users']
# salt=bcrypt.gensalt()
# ab= 'hunter1'
# password= b'hunter'
# collection.insert_one({'username':'Rhitam', 'email':'rhitamdeb26@gmail.com', 'passwordhash': bcrypt.hashpw(password,salt)})

# s="abcacbqsdfgs"

# dict={}
# subs=""
# oldSubs=""
# longSunstring=""
# for  i in s:
#     if i not in dict :
#         subs = subs+i
#         print(s.index(i))
#         dict[i]= s.index(i)
#     else:
#         if len(oldSubs)<len(subs):
#             longSunstring= subs
#         else:
#             oldSubs=subs
#         subs=""

# print(longSunstring)
num1 = [1,3]
num2= [2]
sortedNums= []

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:

        newNums= [*nums1, *nums2]
        print(newNums)
        newNums.sort()
        print(newNums)
        lstLen= len(newNums)
        if  lstLen%2 ==0:
            meadian= (newNums[int(lstLen/2)-1]+newNums[int(lstLen/2)])/2
            return(float(meadian))
        else:
            meadian= newNums[int(lstLen/2)]
            return(float(meadian))



meadian = findMedianSortedArrays(num1, num2)



movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#exercise 1
user_input = input()
def is_good(m, some_movies):
  for i in some_movies:
    if i["name"] == m and i["imdb"] > 5.5:
      return True
  return False

if(is_good(user_input, movies)):
  print("True")
else:
  print("False")


#exercise 2
def is_sublist(some_movie):
  sublist = []
  for i in some_movie:
    if i["imdb"] > 5.5:
      sublist.append(i["name"])
  print(sublist)

is_sublist(movies)

#exercise 3
user_input = input()
def is_category(user_input, movList):

  sublist=[]
  for mov in movList:
    if mov["category"]==user_input:
      sublist.append(mov["name"])  
  print(sublist)

is_category(user_input, movies)

#exercise 4
some_list=input().split()
def is_average(m, some_movies):
  sum=0
  for i in m:
    for mov in some_movies:
      if mov["name"]==i:
        sum+=mov["imdb"]
  print(sum/len(m))

is_average(some_list, movies)


#exercise 5
user_input=input()
def is_average2(user_input, some_movies):
  sum=0
  score=0
  for mov in some_movies:
    if mov["category"]==user_input:
      sum+=mov["imdb"]
      score+=1
  print(sum/score)

is_average2(user_input, movies)
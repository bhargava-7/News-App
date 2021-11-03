from googlesearch import search
#write your query
query = "https://hackr.io/blog/best-python-courses"
# displaying 10 results from the search
for i in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(i)

https://datamahadev.com/10-amazing-python-hacks-with-cool-libraries/    
https://skillcrush.com/blog/python-programming-examples/#:~:text=25%2B%20Python%20Programming%20Examples.%201%201.%20Remove%20Duplicates,Email.%205%205.%20Temperature%20Conversion%20Program.%20More%20items

def save_news(request):
    def favorite(request, pk):
     if request.method == 'POST':
        favorite = Deal.objects.get(pk=pk)
        user = request.user
        user.favorites.add(favorite)
        messages.add_message(request, messages.INFO, 'Deal Favorited.')
        return redirect('home')
favorites = models.ManyToManyField(Deal, related_name='favorited_by')
from googlesearch import search
#write your query
query = "https://hackr.io/blog/best-python-courses"
# displaying 10 results from the search
for i in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(i)

https://datamahadev.com/10-amazing-python-hacks-with-cool-libraries/    
https://skillcrush.com/blog/python-programming-examples/#:~:text=25%2B%20Python%20Programming%20Examples.%201%201.%20Remove%20Duplicates,Email.%205%205.%20Temperature%20Conversion%20Program.%20More%20items

def save_news(request):
    def favorite(request, pk):
     if request.method == 'POST':
        favorite = Deal.objects.get(pk=pk)
        user = request.user
        user.favorites.add(favorite)
        messages.add_message(request, messages.INFO, 'Deal Favorited.')
        return redirect('home')
favorites = models.ManyToManyField(Deal, related_name='favorited_by')
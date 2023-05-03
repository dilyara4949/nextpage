from api.models.book import Book
from api.models.category import Category
from django.http.response import HttpResponse, JsonResponse 
from api.serializers.book import BookSerializer2
def books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer2(books,many=True)
        return JsonResponse(
            serializer.data, safe=False,json_dumps_params={'indent' : 2}
        )
        # return JsonResponse(
        #     list(Book.objects.values()), safe=False,json_dumps_params={'indent' : 2}
        # )
    if request.method == 'POST':
        data = json.loads(request.body)
        book_title = data.get('title','')
        book_author = data.get('author','')
        book_category = Category.objects.get(id=data.get('category',''))
        book_description = data.get('description','')
        book_pages = data.get('pages','')
        book = Book.objects.create(title=book_title,author=book_author,category=book_category,description=book_description,pages=book_pages)
        return JsonResponse(book.to_json(),safe=False, json_dumps_params={'indent': 2})
def book_by_id(request, id):
    try:
        book = Book.objects.get(id=id)
    except:
        pass
    if request.method == 'GET':
        serializer = BookSerializer2(book,many=False)
        return JsonResponse(serializer.data, safe=False,json_dumps_params={'indent' : 2})
    
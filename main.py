
"""  def favAlbum(request, album_id):
    album=get_object_or_404(Album, id=album_id)
    try: 
        selected_album = album.album_set.get(title=request.POST['album']) 
    except (KeyError, Album.DoesNotExist): 
        return render(request, 'fpage/index.html',{
            'album' : album , 
            'error_message' : "you didn't select a valid album"}) 
    else: 
        selected_album.is_favorite1 = True 
        selected_album.save()   
        return render(request, 'fpage/index.html' , {'all_albums' : album})

class BlogSearchListView(BlogListView):
            
            paginate_by = 10

            def get_queryset(self):
                result = super(BlogSearchListView, self).get_queryset()

                query = self.request.GET.get('q')
                if query:
                    query_list = query.split()
                    result = result.filter(
                        reduce(operator.and_,
                            (Q(title__icontains=q) for q in query_list)) |
                        reduce(operator.and_,
                            (Q(content__icontains=q) for q in query_list))
                    )

                return result """

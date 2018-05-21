Quick notes (Notes for self) taken from guides

The first part identifies which template is missing. In this case, it's the articles/new template. Rails will first look for this template. If not found, then it will attempt to load a template called application/new. It looks for one here because the ArticlesController inherits from ApplicationController.

Notice that inside the create action we use render instead of redirect_to when save returns false. The render method is used so that the @article object is passed back to the newtemplate when it is rendered. This rendering is done within the same request as the form submission, whereas the redirect_to will tell the browser to issue another request.

This will now render the partial in app/views/comments/_comment.html.erb once for each comment that is in the @article.comments collection. As the render method iterates over the @article.comments collection, it assigns each comment to a local variable named the same as the partial, in this case comment which is then available in the partial for us to show.

    @comment = @article.comments.create(comment_params)

    @comment = @article.comments.find(params[:id])



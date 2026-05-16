from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Lore, Comment
from .forms import CommentForm
from .forms import LoreForm

# Create your views here.
class LoreList(generic.ListView):
    queryset = Lore.objects.filter(status=1)
    template_name = "the_edda_library/the_edda_library.html"
    paginate_by = 6

    def get_queryset(self):
        """
        Override the default queryset to allow sorting based on query parameters.

        **Context:**

        `sort_by`
            A string obtained from the query parameters that determines the sorting order.

        **Template**

        :template:`the_edda_library/the_edda_library.html`
        
        """
        queryset = super().get_queryset()
        sort_by = self.request.GET.get("sort", "newest")

        if sort_by == "az":
            return queryset.order_by("title")
        elif sort_by == "za":
            return queryset.order_by("-title")
        elif sort_by == "oldest":
            return queryset.order_by("created_on")
        else:  # Default to newest
            return queryset.order_by("-created_on")
        
    def get_context_data(self, **kwargs):
        """
        Override the default context data to include the current sort parameter.

        **Context:**

        `current_sort`
            A string indicating the current sorting order.

        **Template**

        :template:`the_edda_library/the_edda_library.html`

        """
        context = super().get_context_data(**kwargs)
        context["current_sort"] = self.request.GET.get("sort", "newest")
        return context
    
def lore_detail(request, slug):
    """
    View function to display the details of a specific lore entry and its comments as well as functionality to edit.

    **Context:**

    `lore`
        An instance of the Lore model corresponding to the provided slug.

    `comments`
        A queryset of all comments associated with the lore entry.

    `comment_count`
        The number of approved comments for the lore entry.

    **Template**

    :template:`the_edda_library/lore_detail.html`

    """
    queryset = Lore.objects.filter(status=1)
    lore = get_object_or_404(queryset, slug=slug)
    comments = lore.comments.all().order_by("-created_on")
    comment_count = lore.comments.filter(approved=True, parent__isnull=True).count()
    comment_form = CommentForm()
    edit_lore_form = LoreForm(instance=lore)

    if request.method == "POST":

        if "submit_comment" in request.POST:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.lore = lore

                parent_id = request.POST.get("parent_id")
                if parent_id:
                    comment.parent = Comment.objects.get(id=parent_id)
                comment.save()

                messages.add_message(request, messages.SUCCESS, "Your comment has been submitted and is awaiting approval.")
                return redirect("lore_detail", slug=lore.slug)

        if "submit_edit_lore" in request.POST:
            edit_lore_form = LoreForm(data=request.POST, instance=lore, files=request.FILES)
            if edit_lore_form.is_valid():
                lore = edit_lore_form.save(commit=False)
                lore.status = 0
                lore.save()
                edit_lore_form.save_m2m()
                messages.add_message(request, messages.SUCCESS, "The saga has been re-forged. Awaiting Mimir's approval")
                return redirect("library")
        
    return render(request, "the_edda_library/lore_detail.html", {"lore": lore, "comments": comments, "comment_count": comment_count, "comment_form": comment_form, "edit_lore_form": edit_lore_form})


def comment_edit(request, slug, comment_id):
    """
    View to enable users to edit their own comments
    """

    if request.method == "POST":
        queryset = Lore.objects.filter(status=1)
        lore = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.lore = lore
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated! Pending approval.')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return redirect("lore_detail", slug=lore.slug)

def comment_delete(request, slug, comment_id):
    """
    View to enable users to delete their own comments
    """
    queryset = Lore.objects.filter(status=1)
    lore = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment Deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return redirect("lore_detail", slug=lore.slug)
    
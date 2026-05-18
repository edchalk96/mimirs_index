/** Function to toggle a reply in comments thread */

function toggleReply(id) {
    const replyForm = document.getElementById('reply-' + id);
    replyForm.classList.toggle('d-none');
}

const editButtons = document.getElementsByClassName("edit-btn");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const commentHeading = document.getElementById("commentHeading")

const deleteModal = new bootstrap.Modal(document.getElementById("deleteCommentModal"));
const deleteButtons = document.getElementsByClassName("comment-delete-btn");
const deleteConfirm = document.getElementById("deleteConfirm");

/** Functionality to edit comments */

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.currentTarget.getAttribute("data-comment_id");
        let commentContent = document.getElementById(`body-${commentId}`).innerText.trim();
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentHeading.innerText = "Update Comment"
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
        commentForm.scrollIntoView({ behavior: 'smooth' });
    })
}

/** Functionality for deletion of comments */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.currentTarget.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}
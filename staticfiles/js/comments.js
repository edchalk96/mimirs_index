/** Function to toggle a reply in comments thread and ensure empty reply text area */

function toggleReply(id) {
    const replyForm = document.getElementById('reply-' + id);
    replyForm.classList.toggle('d-none');

    if (!replyForm.classList.contains('d-none')) {
        const replyTextArea = replyForm.querySelector('textarea');
        if (replyTextArea) {
            replyTextArea.value = '';
        }
    }
}

const editButtons = document.getElementsByClassName("edit-btn");
const commentForm = document.getElementById("commentForm");
const commentText = commentForm ? commentForm.querySelector("textarea") : null;

const submitButton = document.getElementById("submitButton");
const commentHeading = document.getElementById("commentHeading");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteCommentModal"));
const deleteButtons = document.getElementsByClassName("comment-delete-btn");
const deleteConfirm = document.getElementById("deleteConfirm");

/** Functionality to edit comments */

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.currentTarget.getAttribute("data-comment_id");

        let bodyElement = document.getElementById(`body-${commentId}`);
        if (!bodyElement) return;
        
        let commentContent = bodyElement.innerText.trim();

        if (commentText) {
            commentText.value = commentContent;
        }

        submitButton.innerText = "Update";
        commentHeading.innerText = "Update Comment";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
        commentForm.scrollIntoView({ behavior: 'smooth' });
    });
}

/** Functionality for deletion of comments */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.currentTarget.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}
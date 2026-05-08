/** Function to toggle a reply in comments thread */

function toggleReply(id) {
    const replyForm = document.getElementById('reply' + id);
    replyForm.classList.toggle('d-none');
}

const editButtons = document.getElementsByClassName("edit-btn");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/** Functionality to edit comments */

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    })
}

/** Functionality for deletion of comments */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}
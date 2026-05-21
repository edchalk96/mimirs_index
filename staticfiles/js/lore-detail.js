/* Function for select fiels in a bootstrap modal */
document.addEventListener("DOMContentLoaded", function () {
    const editLoreModal = document.getElementById('editLoreModal');
    if (editLoreModal) {
        $(editLoreModal).on('shown.bs.modal', function () {
            const selectField = $('#editLoreModal select');
            if (selectField.length > 0) {
                selectField.select2({
                    placeholder: "Select entities...",
                    allowClear: true,
                });
                selectField.trigger('change');
            }
        });
    }
});
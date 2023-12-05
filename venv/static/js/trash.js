function toggleDeleteButton() {
    var checkboxes = document.querySelectorAll('.mail-item input[type="checkbox"]');
    var deleteButton = document.querySelector('.delete-button');

    var checkedCount = 0;
    checkboxes.forEach(function (checkbox) {
        if (checkbox.checked) {
            checkedCount++;
        }
    });

    if (checkedCount > 0) {
        deleteButton.style.display = 'inline-block';
    } else {
        deleteButton.style.display = 'none';
    }
}

function deleteSelected() {
    var checkboxes = document.querySelectorAll('.mail-item input[type="checkbox"]');
    checkboxes.forEach(function (checkbox) {
        if (checkbox.checked) {
            // Perform delete action for the selected item
            checkbox.closest('.mail-item').remove();
        }
    });

    // After deletion, hide the delete button
    var deleteButton = document.querySelector('.delete-button');
    deleteButton.style.display = 'none';
}

function toggleSelectAll() {
    var selectAllCheckbox = document.getElementById('selectAll');
    var checkboxes = document.querySelectorAll('.mail-item input[type="checkbox"]');

    checkboxes.forEach(function (checkbox) {
        checkbox.checked = selectAllCheckbox.checked;
    });

    // Update the delete button visibility based on the state of the checkboxes
    toggleDeleteButton();
}

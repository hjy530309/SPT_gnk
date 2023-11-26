function sendEmail() {
    // 메일 전송 로직을 추가할 수 있습니다.
    console.log('메일 전송!');
}

function switchTab(tabName) {
    // 탭 간 전환 로직
    document.querySelectorAll('.mail-tabs button').forEach(function (tabButton) {
        tabButton.classList.remove('active-tab');
    });

    document.querySelectorAll('.mail-content').forEach(function (content) {
        content.classList.add('hidden');
    });

    document.getElementById(tabName + '-tab').classList.add('active-tab');
    document.getElementById(tabName + '-content').classList.remove('hidden');
}
function sendEmail() {
    var recipient = document.getElementById('recipient').value;
    var subject = document.getElementById('subject').value;
    var message = document.getElementById('message').value;
    var attachment = document.getElementById('attachment').files[0];
    var contacts = document.getElementById('contacts').value;

    // 예시로 콘솔에 출력
    console.log('메일 전송:', {
        recipient: recipient,
        subject: subject,
        message: message,
        attachment: attachment,
        contacts: contacts
    });
}
function addNewContact() {
    // Get the input field and select dropdown
    var newContactInput = document.getElementById('newContact');
    var contactsDropdown = document.getElementById('contacts');
    var newContactInputWrapper = document.getElementById('newContactInputWrapper');

    // Get the value from the input field
    var newContactValue = newContactInput.value.trim();

    // If the input is not empty, add it to the dropdown
    if (newContactValue !== '') {
        // Create a new option element
        var newOption = document.createElement('option');

        // Set the value and text of the new option
        newOption.value = 'contact' + (contactsDropdown.options.length + 1);
        newOption.text = newContactValue;

        // Append the new option to the dropdown
        contactsDropdown.add(newOption);

        // Clear the input field
        newContactInput.value = '';
    }

    // Hide the input field after adding the new contact
    newContactInputWrapper.style.display = 'none';
}

function toggleNewContactInput() {
    var newContactInputWrapper = document.getElementById('newContactInputWrapper');

    // Toggle the display property (show if hidden, hide if shown)
    if (newContactInputWrapper.style.display === 'none' || newContactInputWrapper.style.display === '') {
        newContactInputWrapper.style.display = 'block';
    } else {
        newContactInputWrapper.style.display = 'none';
    }
}
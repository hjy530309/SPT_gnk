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
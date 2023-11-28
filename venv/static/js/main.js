function submitForm() {
    var username = document.getElementById('id').value;
    var password = document.getElementById('pw').value;

    // AJAX 요청
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/submit', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // 성공적으로 서버에서 응답을 받았을 때 실행할 코드
            console.log('Data submitted successfully!');
        }
    };

    var data = {
        username: username,
        password: password
    };

    xhr.send(JSON.stringify(data));
}

function signup(){
    window.location.href = 'sign1.html';

}

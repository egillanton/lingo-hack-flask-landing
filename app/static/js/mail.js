//////// SEND EMAIL /////////////////////////////////
function sendEmail() {
    let input_name = strip($("#input_name").val());
    let input_phone = strip($("#input_phone").val());
    let input_email = strip($("#input_email").val());
    let input_subject = strip($("#input_subject").val());
    let input_message = strip($("#input_message").val());

    if (input_name &&
        input_phone &&
        input_email &&
        input_subject &&
        input_message) {

        $.ajax({
            type: 'POST',
            url: "/email",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: JSON.stringify({
                "name": input_name,
                "email": input_email,
                "phone": input_phone,
                "subject": input_subject,
                "message": input_message,
            }),
            success: function (res) {
                // Clear Input
                $("#input_name").val("");
                $("#input_phone").val("");
                $("#input_email").val("");
                $("#input_subject").val("");
                $("#input_message").val("");

                Swal.fire(
                    'Email was sent!',
                    'We will be in touch!',
                    'success'
                );
            },
            error: function (error) {
                Swal.fire(
                    'Email was not sent!',
                    'please send us a message at egilla14@ru.is',
                    'error'
                );
            },
        });

    } else {
        Swal.fire(
            'Email not sent!',
            'Please fill in all the fields!',
            'warning'
        );
    }


}

//////// STRIP HTML /////////////////////////////////
function strip(html) {
    var tmp = document.createElement("DIV");
    tmp.innerHTML = html;
    return tmp.textContent || tmp.innerText || "";
}
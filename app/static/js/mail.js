//////// SEND EMAIL /////////////////////////////////
function sendEmail() {
    var input_name = $("#input_name").val();
    var input_phone = $("#input_phone").val();
    var input_email = $("#input_email").val();
    var input_subject = $("#input_subject").val();
    var input_message = $("#input_message").val();
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
}
$(document).ready(function(){
    $("#contact").submit(function(event){
        event.preventDefault();  // جلوگیری از ارسال فرم به صورت معمولی
        $.ajax({
            type: 'POST',
            url: contactUrl,
            data: $(this).serialize(),
            success: function(data){
                showMessage("پیام شما با موفقیت دریافت شد", "success");
                $("#contact")[0].reset();  // پاک کردن فرم
            },
            error: function(xhr, errmsg, err) {
                let errorMessage;
                if (xhr.status === 400) {
                    errorMessage = "خطای نامعتبر بودن فرم";
                } else if (xhr.status === 500) {
                    errorMessage = "خطای ارتباط با سرور";
                } else {
                    errorMessage = "خطای نامشخص رخ داد: " + xhr.status;
                }
                showMessage(errorMessage, "error");
            }
        });
    });
});

function showMessage(message, type) {
    const messageBox = document.getElementById('message-box');
    messageBox.innerText = message;
    messageBox.className = type === "success" ? "success-message" : "error-message"; // تعیین کلاس بر اساس نوع پیام
    messageBox.style.display = 'block';
    setTimeout(() => {
        messageBox.style.display = 'none';
    }, 4000); // پیام بعد از ۴ ثانیه ناپدید می‌شود
}


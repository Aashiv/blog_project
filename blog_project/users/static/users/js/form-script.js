$(document).ready(function() {
    $("#contactForm").validate({
        rules: { /* Define rules: required, email, minlength */ },
        submitHandler: function(form) {
            $.ajax({
                url: "your-api-endpoint",
                type: "POST",
                data: $(form).serialize(), // Converts form data for submission
                success: function(response) { /* Show success message */ }
            });
        }
    });
});
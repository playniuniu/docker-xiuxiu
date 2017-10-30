$(document).ready(function () {
    $("#submit-btn").on("click", function(event){
        event.preventDefault();
        $("#demo-form").submit();
    });
});

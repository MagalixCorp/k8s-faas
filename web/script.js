$(document).ready(function () {
    $("#submit").click(function () {
        $.ajaxSetup({
            contentType: "application/json; charset=utf-8"
        });
        url = $("#url").val()
        data = JSON.stringify({
            "url": url
        })
        $.post("/api/", data).done(function (data) {
            $("#result").html("Thank you. The URL is being scraped now")
        })
    })
});
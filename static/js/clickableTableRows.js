// look through all table row
$("tr").each(function () {
    // if there is an href attr
    if ($(this)[0].getAttribute("href") != null) {
        // have the cursor change to a pointer on hover
        $(this)[0].style.cursor = "pointer"
        // add a click event listener to navigate to the specified url
        $(this).click(function () {
            href = $(this)[0].getAttribute("href")

            if ($(this)[0].hasAttribute("pop")) {
                popitup(href, 'popoutWindow')
            } else {
                document.location.href = href
            }

        });
    }
});

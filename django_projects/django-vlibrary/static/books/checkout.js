$( "#check-out" ).click(function() {
    const checkboxes = $('input:checkbox:checked')
    console.log(checkboxes)
    checkboxes.each(function() {
        console.log(this.name)
    })
})



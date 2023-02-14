document.addEventListener("DOMContentLoaded", function()
{
    var letterInput = document.querySelector("input[name='letter_guess']");
    letterInput.addEventListener("input", function(event)
    {
        var letter = event.target.value;
        if (letter.length > 1)
        {
            letterInput.value = letter[0];
        }
    });
});
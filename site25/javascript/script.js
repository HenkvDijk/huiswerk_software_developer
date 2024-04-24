$(document).ready(function () {
    // Verberg de paragrafen en verklein hun lettergrootte bij het klikken op #hidep
    $("#hidep").click(function () {
        $("p").hide().animate({ fontSize: '1em' }, "slow");
    });

    // Toon de verborgen paragrafen bij het klikken op #showp
    $("#showp").click(function () {
        $("p").show().animate({ fontSize: '1em' }, "slow");
    });

    // Verberg een paragraaf als erop wordt geklikt
    $("p").click(function () {
        $(this).hide("slow", function () { alert("Zo, en nu is de tekst dus weg. Goed gedaan") });
    });

    // Vergroot de lettergrootte van de paragrafen bij het klikken op #vergroot
    $("#vergroot").click(function () {
        $("p").show().animate({ fontSize: '3em' }, "slow");
    });

    // Verklein de lettergrootte van de paragrafen bij het klikken op #verklein
    $("#verklein").click(function () {
        $("p").show().animate({ fontSize: '.6em' }, "slow");
    });

    // Titel van kleur veranderen door muispijlje
    $(".titel").on({
        mouseenter: function () {
            $(this).css("background-color", "lightblue");
        },
        mouseleave: function () {
            $(this).css("background-color", "grey");
            $(this).css("color", "white");
        },
        click: function () {
            $(this).css("color", "darkgrey");
        }
    });

    //Keuzemenu kleuren verschijnt na dubbelklik
    $("#flip").dblclick(function () {
        $("#panel").slideToggle("slow");
    });

    // Achtergrondkleur body instellen
    $("#wit").click(function () {
        $("body").css("background-color", "white");
    })
    $("#grijs").click(function () {
        $("body").css("background-color", "lightgrey");
    })
    $("#blauw").click(function () {
        $("body").css("background-color", "lightblue");
    })

});



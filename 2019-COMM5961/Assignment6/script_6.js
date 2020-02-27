$(document).ready(function(){

    $("button#hide_h2").click(function() {
        $("h2").hide(500);
    });

    $("button#show_h2").click(function() {
        $("h2").show(300);
        $("h2").css("color","blue");
        $("h2").html("You clicked me hard.");
    });

    $("button#clear_screen").click(function() {
        var $x = $("container");
        $x.empty();
    });

    $("button#get_data").click(function() {
        var items = [];
        var i = 0;
        var airtable_read_endpoint = "https://api.airtable.com/v0/appZWJSXtBaJSsesN/higashino?api_key=keySjh71YKM5KPkDF ";
        var dataSet = [];
        $.getJSON(airtable_read_endpoint, function(result) {
               $.each(result.records, function(key,value) {
                   items = [];
                       items.push(value.fields.Book_name);
                       items.push(value.fields.Book_rating);
                       items.push(value.fields.Attachments);
                       items.push(value.fields.Translator);
                       items.push(value.fields.Publisher);
                       items.push(value.fields.Publish_Year);
                       items.push(value.fields.Price);
                       dataSet.push(items);
                       console.log(items);
                }); // end .each
                console.log(dataSet);

             $('#table1').DataTable( {
                 data: dataSet,
                 retrieve: true,
                 columns: [
                     { title: "Book",
                       defaultContent:""},
                     { title: "Rating",
                       defaultContent:"" },
                     { title: "Cover",
                       defaultContent:"" },
                     { title: "Translator",
                       defaultContent:""},
                     { title: "Publisher",
                       defaultContent:""},
                     { title: "Publishing_year",
                       defaultContent:""},
                       { title: "Price(RMB)",
                       defaultContent:""}
                 ]
             } );
        }); // end .getJSON
     }); // end button

}); // document ready

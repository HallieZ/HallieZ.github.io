$(document).ready(function(){
$("button#get_data").click(function() {
   var items = [];
    var i = 0;
    var airtable_read_endpoint = "https://api.airtable.com/v0/app5018SLfPUcQe9o/Author_work?api_key=keySjh71YKM5KPkDF";
    var dataSet = [];
    $.getJSON(airtable_read_endpoint, function(result) {
           $.each(result.records, function(key,value) {
               items = [];
                   items.push(value.fields.name);
                   items.push(value.fields.Count);
                   dataSet.push(items);
                   console.log(items);
            }); // end .each
            console.log(dataSet);

            var chart = c3.generate({
                data: {
                    columns: dataSet,
                    type : 'bar'
                },
                axis: {
                  x: {label: 'Author'},
                  y: {label: '# of Works'}
                },
                bar: {
                    title: "# of Works by Author:",
                }
            });

        })})}); // document ready


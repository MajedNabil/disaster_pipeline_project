


let data = [];
let labels = [];



window.addEventListener('load', shadi);

function renderChart(data, labels, name, id) {
    console.log("functions gets executed");
    var ctx = document.getElementById(id).getContext('2d');

    var myChart = new Chart(ctx, {
        type: name,
        data: {
            labels: labels,
            datasets: [{
                label: 'This week',
                data: data,
            }]
        },

    });

}


async function shadi ()  {
     new_freq = $('#name').val() //value I want to send
    console.log("jkdkdkdkdkdkdkdkdk hlll");
    await $.ajax({
    url: '/repl',
    type: 'POST',
    data: new_freq,
    success: function(response){

        console.log("EHEHEHHHEHEH:    " + response[0][4])
        var counter = 0;
        var socialCounter = 0;
        var directCounter = 0;
        var newsCounter = 0;

        for(var i=0; i<26216; i++){
            console.log(response[i][4])
            if(response[i][4] === "social"){
                socialCounter ++;
            }else if(response[i][4] === "news"){
                newsCounter ++;
            }else if(response[i][4] === "direct"){
                directCounter++;
            }
        }
        labels = ["direct" , "news" , "social"]
        data = [directCounter , newsCounter , socialCounter]

        renderChart(data, labels, 'bar', "myChart1");
    renderChart(data, labels, 'doughnut', "myChart2");
    document.getElementById("myChart1").style.display = 'block';
        document.getElementById("myChart2").style.display = 'block';

     $(".loader-wrapper").fadeOut("slow");

        var glo = socialCounter + directCounter + newsCounter;
        console.log("TOTAL:   "+ glo);
    }
})
}








function submitSentence(){


  new_freq = $('#name').val() //value I want to send
 console.log("HELLO WORLD:   " + new_freq)
$.ajax({
    url: '/predict',
    type: 'POST',
    content_type : "application/json",
    data: {'message' : new_freq},
    success: function(response){

     console.log("RESPONSE:  " + response.length)
        var counter = 0;
       while(response[counter] != null ){
         console.log(counter + " REG: " + response[counter][counter])
           counter++;
       }
    }
})

}

console.log("START")

function plus(a,b) {
    var c = 0;
    a = parseInt(a);
    b = parseInt(b);
    d = Math.abs(a-b)
    c = (a+b)*(d+1)/2;
    return c;
  }

function ask_answer(){
    var a = document.getElementById("myForm").elements[0].value;
    var b = document.getElementById("myForm").elements[1].value;
    var c = plus(a,b);
    var e = document.getElementById("hpm");
      e.style.fontSize = "25px";
      e.style.color = "red";
    document.getElementById("hpm").innerHTML = "The answer is " + c;
}
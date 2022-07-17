
//print date to log
const d = Date();
console.log(d);

//pull the pathname from window location
const activePage = window.location.pathname;
console.log(window);
console.log(window.location);
console.log(activePage);

/*create an arey of the links in nav, 
compare each to pathname and mark the one that is active
*/ 
const links = document.querySelectorAll('nav a').forEach(link => {    
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});


var check = function() {
  if (document.getElementById('password').value ==
    document.getElementById('confirm_password').value) {
    document.getElementById('message').style.fontSize = 'large';
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerHTML ='Passwords are matching';
  } else {
    document.getElementById('message').style.fontSize = 'large';
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerHTML ='Passwords are not matching';
  }

}

var validateMyForm = function(){
  if (document.getElementById('password').value ==
    document.getElementById('confirm_password').value ) {
    return true;
  } else {
    alert("Passwords are not matching");
    return false;
  }
}

var checkNumbers = function(){
  var ccnumber=document.getElementById('ccnumber').value
  var cvv=document.getElementById('cvv').value
  if (ccnumber.length==16 && cvv.length==3 ) {
    return true;
  } else {
    alert("Credit card details are incorrect");
    return false;
  }

}
function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}

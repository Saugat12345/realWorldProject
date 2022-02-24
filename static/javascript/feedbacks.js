const userName = document.querySelector('#name');
const userEmail = document.querySelector('#email');
const hiddenDiv = document.querySelector('#innerDiv');
const btn = document.getElementById('submitbtn');

btn.addEventListener('click', btnClicked);

function btnClicked(e){
    e.preventDefault();
    if (userName.value === '' || userEmail.value === ''){
        innerDiv.innerHTML = "<h2> Please fill out all the credentials! </h2>";
        setTimeout(() => hiddenDiv.remove(), 7000);
    }
    else{
        innerDiv.innerText = `Thank You   ${userName.value}. We will reach you via your email : ${userEmail.value}`;
        setTimeout(() => innerDiv.remove(), 5000);
    }
    //Clearing the fields
    userName.value = '';
    userEmail.value = '';
}
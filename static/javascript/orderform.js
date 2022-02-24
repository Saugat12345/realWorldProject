const checkbox = document.getElementById('validation');
const btn = document.getElementById('submitbtn');

const quantity = document.querySelector('#quantity');
var productPrice = document.getElementById("price").value;

btn.onclick = function total(e){
    e.preventDefault();
    if (checkbox.value === ''){
        innerDiv.innerHTML = "<h2> Please Check this Checkbox </h2>";
        setTimeout(() => hiddenDiv.remove(), 7000);
    }
    else{
        var total = (quantity.value) * (productPrice);
        innerDiv.innerText = `Thank You. Your Total is ` + total;
        setTimeout(() => innerDiv.remove(), 7000);
    }
}




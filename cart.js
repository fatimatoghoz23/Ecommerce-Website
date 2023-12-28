var updateBtns=document.getElementsByClassName('update-cart')
for(var i =0;i<updateBtns.length;i++){
  updateBtns[i].addEventListener('click',function(){
    var productId=this.dataset.product
    var action=this.dataset.action
    console.log('productId',productId,'action:',action)
    console.log("user:", user)
    if(user==='AnonymousUser'){
      addCookieItem(productId, action)
    }else{
			updateUserOrder(productId, action)
    }

  })
}

function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

	var url = '/update_item/'//نحدد لوين نرسلها (api)

  fetch(url, {
		method:'POST',//حددنا نوعها
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,  //script in products
		}, 
		body:JSON.stringify({'productId':productId , 'action':action})
	})
  .then((response) => {//لتحويل لبيانات json
		return response.json()
	})
	.then((data) => {//التحكم بالبيانات
		console.log('data:' , data)
		location.reload()

	});
}

function addCookieItem(productId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	location.reload()

}










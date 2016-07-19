var user = (function(){
	var isLoggedIn = true;

	var login = function(){
		var $form = $('#loginForm');
		
	}

	var register = function(){

	}
}());

$(document).ready(function(){
	// $("#header").load("/static/partials/header.html");
    // $("#footer").load("/static/partials/footer.html");
    // $("#sidebar").load("/static/partials/sidebar.html");
    // $("#content").load("/static/partials/home.html");	
})

function load_products(){
    $("#content").load("/static/partials/products.html", function(){
	    populate_product_list();
    });
}

function add_product(){
    $("#content").load("/static/partials/forms/add_product.html");
}

function add_order(){
	 $("#content").load("/static/partials/forms/add_order.html");
}

function add_customer(){
	$("#content").load("/static/partials/forms/add_customer.html");
}

function add_supplier(){
	$("#content").load("/static/partials/forms/add_supplier.html");
}

function populate_product_list(){
	// This is just dummy data
	var product_div = $('#product_list');
	product_list = [ 
		{'sku':'12345', 'title':'Title1', 'description':'Description1'},
		{'sku':'12345', 'title':'Title1', 'description':'Description1'},
		{'sku':'12345', 'title':'Title1', 'description':'Description1'},
		{'sku':'12345', 'title':'Title1', 'description':'Description1'},
		{'sku':'12345', 'title':'Title1', 'description':'Description1'},
		{'sku':'12345', 'title':'Title1', 'description':'Description1'},
		{'sku':'12345', 'title':'Title1', 'description':'Description1'},
		{'sku':'12345', 'title':'Title1', 'description':'Description1'},
	]
	len = product_list.length
	html = '';
	for (var i = 0; i < len; i++){
		html += '<tr>' + 
    		'<td>'+ product_list[i].sku +'</td>' + 
    		'<td>'+ product_list[i].title +'</td>' +
    		'<td>'+ product_list[i].description +'</td>' +
    	'</tr>';
	}
	console.log(html);
	product_div.append(html);
}



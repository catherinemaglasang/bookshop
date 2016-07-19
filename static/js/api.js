
$(document).ready(function(){
	// This tells javascript to immediately load task on browser load. Hence, we won't be needing load tasks button.
	add_new_product();

	$("new_product_form").submit(function(event){
		console.log("SUBMIT");
		event.preventDefault();
		console.log("SUBMIT");
		$.ajax({
			url: 'http://127.0.0.1:5000/api/v1/products/',
			type: "POST",
			data: $("new_product_form").serialize(),
			cache: false,
			contentType: false,
			processData: false,
			success: function(resp) {
				if (resp.status  == 'ok') {
					console.log(resp);
					add_new_product();
				} else {
					alert(resp.message);
				}
			},
			error: function (e) {
				alert("danger " + e.status);
			}
		})

	});
})

function populate_row(id, sku, supplier_id, title, description, category_id, unit_price, on_hand, reorder_product, is_active){
	return 	'<tr>' +
				'<td>' + id + '</td>' +
				'<td>' + sku + '</td>' +
				'<td>' + supplier_id + '</td>' +
				'<td>' + title + '</td>' +
				'<td>' + description + '</td>' +
				'<td>' + category_id + '</td>' +
				'<td>' + unit_price + '</td>' +
				'<td>' + on_hand + '</td>' +
				'<td>' + reorder_product + '</td>' +
				'<td>' + is_active + '</td>' +
				'<td><a onclick="delete_product('+id+')" class="btn btn-small btn-danger" href="javascript:void(0)">Delete</a></td>' +
				// '<td><a onclick="update_product('+id+')" class="btn btn-small btn-primary" href="#">Update</a></td>' +
			'</tr>';
}

function delete_product(id){
	$.ajax({
		url: 'http://127.0.0.1:5000/api/v1/products/' + id + '/',
		type:"DELETE",
		dataType: "json",
		success: function(resp) {
			if (resp.status  == 'ok') {
				console.log(resp);
				add_new_product();
			} else {
				alert(resp.message);
			}
		},
		error: function (e) {
			alert("danger " + e.status);
			}
			//   beforeSend: function (xhrObj){
			// 	xhrObj.setRequestHeader("Authorization",
			// 		  "Basic " + btoa("ako:akolagini"));
			// }
	});
}


function add_new_product() {
	$.ajax({
		url: 'http://127.0.0.1:5000/api/v1/products/',
		type:"GET",
		dataType: "json",
		success: function(resp) {
			$("#products").html("");
			if (resp.status  == 'ok') {
			   	for (i = 0; i < resp.count; i++)
				{
					 description = resp.entries[i].description;
					 done = resp.entries[i].done;
					 id = resp.entries[i].id;
					 title = resp.entries[i].title;
					 //console.log(resp);
					 $("#products").append(populate_row(id, sku, supplier_id, title, description, category_id, unit_price, on_hand, reorder_product, is_active));
				}
			} else {
				$("#products").html("");
				alert(resp.message);
			}
		},
		error: function (e) {
			alert("danger " + e.status);
			}
			//   beforeSend: function (xhrObj){
			// 	xhrObj.setRequestHeader("Authorization",
			// 		  "Basic " + btoa("ako:akolagini"));
			// }
	});
}



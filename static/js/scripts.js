function confirmProductDelete(product_id){
  console.log(product_id);
  var r = confirm('Are you sure?'); 
  if (r==true) 
    window.location = '/dashboard/delete_product/' + product_id + '/'; 
  else 
    window.location = '/dashboard/products/';
}


function confirmCategoryDelete(category_id){
  console.log(category_id);
  var r = confirm('Are you sure?'); 
  if (r==true) 
    window.location = '/dashboard/delete_category/' + category_id + '/'; 
  else 
    window.location = '/dashboard/categories/';
}
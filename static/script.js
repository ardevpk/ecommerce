


function quan(id){
    output = `<div class="input-group">
      <span class="input-group-btn">
          <button class="btn btn-white btn-minuse" type="button" onclick="minus(${id})">-</button>
      </span>
      <input type="number" class="form-control no-padding add-color text-center height-25" id="input_${id}" value="0">
      <span class="input-group-btn">
          <button class="btn btn-red btn-pluss" type="button" onclick="plus(${id})">+</button>
      </span>
  </div>`
  document.getElementById(id).innerHTML = output
  $("#btn_"+id).prop('disabled', false);
  }
  
  function minus(id){
      if (parseInt(document.getElementById("input_"+id).value) > 0) {
        document.getElementById("input_"+id).value = parseInt(document.getElementById("input_"+id).value) - 1;
      }
  }
  
  function plus(id){
  document.getElementById("input_"+id).value = parseInt(document.getElementById("input_"+id).value) + 1;
    }
  
  
  
  
  
  function quanb(id){
    output = `<div class="input-group">
      <span class="input-group-btn">
          <button class="btn btn-white btn-minuse" type="button" onclick="minusb(${id})">-</button>
      </span>
      <input type="number" class="form-control no-padding add-color text-center height-25" id="inputb_${id}" value="0">
      <span class="input-group-btn">
          <button class="btn btn-red btn-pluss" type="button" onclick="plusb(${id})">+</button>
      </span>
  </div>`
  document.getElementById(id).innerHTML = output
  $("#btn_"+id).prop('disabled', false);
  }
  
  
  function minusb(id){
    if (parseInt(document.getElementById("inputb_"+id).value) > 0) {
      document.getElementById("inputb_"+id).value = parseInt(document.getElementById("inputb_"+id).value) - 1;
    }
  }
  
  function plusb(id){
  document.getElementById("inputb_"+id).value = parseInt(document.getElementById("inputb_"+id).value) + 1;
  }
  
  
    
  function addfav(id) {
    if (document.getElementById(id).innerHTML == `<i class="bi bi-heart-fill"></i>`) {
      $("#fav_"+id).html(`<div class="spinner-border spinner-border-sm" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>`);
    } else {
      $("#fav_"+id).html(`<div class="spinner-border spinner-border-sm" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>`);
    }
    var token = '{{ csrf_token }}';
    var formData = new FormData()
    formData.append('id', id)
    $.ajax({
        url: "/addtofav/",
        type: 'POST',
        data: formData,
        headers: { 'X-CSRFToken': token },
        processData: false,
        contentType: false,
        success: function (response) {
            let values = response['data']
            if (values == false){
                output = `<i class="bi bi-heart"></i>`
                document.getElementById("fav_"+id).innerHTML = output
                document.getElementById("lblCartCount11").innerText = parseInt(document.getElementById("lblCartCount11").innerText) - 1
                  
              }
            else{
              output = `<i class="bi bi-heart-fill"></i>`
              document.getElementById("fav_"+id).innerHTML = output
              document.getElementById("lblCartCount11").innerText = parseInt(document.getElementById("lblCartCount11").innerText) + 1
                
        }},
        failure: function () {
          swal({
              title: `Failure`,
              text: "Something Went Wrong Please Try Again Later!",
              icon: "error",
            })
        }
    })
  }
  
  
  
  
  
  function addcart(id) {
    let output = `<button class="btn btn-primary" type="button" disabled>
      <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
      Loading...
    </button>`
    $("#btn_"+id).prop('disabled', false);
    document.getElementById("btn_"+id).innerHTML = `<span class="spinner-border spinner-border-sm mx-1" role="status" aria-hidden="true"></span>` + "Adding..."
    var token = '{{ csrf_token }}';
    var formData = new FormData()
    formData.append('id', id)
    if (document.getElementById("inputb_"+id)){
      formData.append('quantityb', parseInt(document.getElementById("inputb_"+id).value))
    } else {
      formData.append('quantity', parseInt(document.getElementById("input_"+id).value))
    }
    $.ajax({
        url: "/add-to-cart/",
        type: 'POST',
        data: formData,
        headers: { 'X-CSRFToken': token },
        processData: false,
        contentType: false,
        success: function (response) {
            let values = response['data']
            if (values == true){
                document.getElementById("lblCartCount").innerHTML = parseInt(document.getElementById("lblCartCount").innerText) + 1
              }
              document.getElementById("btn_"+id).innerHTML = `<i class="bi bi-check2-square mx-2"></i>` + "Added"
            },
        failure: function () {
          swal({
              title: `Failure`,
              text: "Something Went Wrong Please Try Again Later!",
              icon: "error",
            })
        }
    })
  }
  
  
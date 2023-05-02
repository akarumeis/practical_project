// function minusCount() {
//     console.log()
//     // if (+count.innerHTML > 1){
//     //     +count.innerHTML-- ;
//     // }
// }
// function plusCount() {
//     // +count.innerHTML++ ;
// }

$(".minus").click(function (e) {
    e.preventDefault();
    let value = $(this).parent().find("span[class=count]").html();
    +value--
    $(this).parent().find("span[class=count]").html(value);
  });
  
  $(".plus").click(function (e) {
    e.preventDefault();
    let value = $(this).parent().find("span[class=count]").html();
    +value++
    $(this).parent().find("span[class=count]").html(value);
  });
  
  // ------ Счётчик
  
  // ------
  
  $(document).ready(function () {
    $(".send_btn").click(function (e) {
      e.preventDefault();
      const csrf = $("#form").find("input[name=csrfmiddlewaretoken]");
      
      $.ajax({
        url: $(".url").val(),
        type: "POST",
        data: {
          csrfmiddlewaretoken: csrf.val(),
          id: $(this).val(),
          count: $(".count").html(),
        },
        success: function () {},
      });
    });
  });
  
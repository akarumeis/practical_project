$(document).ready(function () {
  const url = $(".url");
  const csrf = $('#form input[name="csrfmiddlewaretoken"]');
  const minusBtn = $(".minus");
  const plusBtn = $(".plus");
  const sendBtn = $(".send_btn");
  const deleteBtn = $(".delete_btn");
  const send_amount_btn = $(".send_amount");

  // console.log($('#price').parent().parent().find('span.amount').html())
  // console.log($('#price').parent().parent().find('span.amount').html())
  // console.log($('.amount').parent().parent().find('input[name=price_one]').val())

  $(".amount").each(function (index, element) {
    let $amount = $(element);
    let $product = $amount.closest(".product");
    let priceOne = +$product.find("input[name=price_one]").val();
    let totalPrice = priceOne * +$amount.text();
    $product.find("span.price_span").html(totalPrice);
  });

  $(".price_span").each(function (index, element) {
    $(".all_price").html(+$(".all_price").html() + +$(element).html());
  });

  minusBtn.click(function (e) {
    e.preventDefault();
    let value = $(this).parent().find("span.amount").html();
    if (+value > 1) {
      --value;
      $(this).parent().find("span.amount").html(value);
    }
  });

  plusBtn.click(function (e) {
    e.preventDefault();
    let value = $(this).parent().find("span.amount").html();
    ++value;
    $(this).parent().find("span.amount").html(value);
  });
  sendBtn.click(function (e) {
    e.preventDefault();
    $.ajax({
      url: url.val(),
      type: "POST",
      data: {
        csrfmiddlewaretoken: csrf.val(),
        product: $(this).val(),
        amount: $(this).parent().find("span.amount").html(),
      },
      success: function () {},
    });
  });

  deleteBtn.click(function (e) {
    e.preventDefault();
    let idForm = $(`#${$(this).val()}`);
    const csrf_del = idForm.find("input[name=csrfmiddlewaretoken]");
    $.ajax({
      url: url.val(),
      type: "POST",
      data: {
        csrfmiddlewaretoken: csrf_del.val(),
        id: $(this).val(),
        button: "delete",
      },
      success: function () {
        idForm.remove();
        $(".all_price").html("0")
        $(".price_span").each(function (index, element) {
          $(".all_price").html(+$(".all_price").html() + +$(element).html());
        });
      },
    });
  });

  send_amount_btn.click(function (e) {
    e.preventDefault();
    let idForm = $(`#${$(this).val()}`);
    const csrf_amount = idForm.find("input[name=csrfmiddlewaretoken]");

    $.ajax({
      url: url.val(),
      type: "POST",
      data: {
        csrfmiddlewaretoken: csrf_amount.val(),
        id: $(this).val(),
        amount: $(this).parent().find("span.amount").html(),
        button: "change_amount",
      },
      success: function () {
        const price_one = idForm.find("input[name=price_one]");
        const amount = idForm.find("span.amount");
        const price = idForm.find("span.price_span");
        price.html(+price_one.val() * +amount.html());
        $(".all_price").html("0")
        $(".price_span").each(function (index, element) {
          $(".all_price").html(+$(".all_price").html() + +$(element).html());
        });
      },
    });
  });
});

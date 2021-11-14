const write_meal = () => {
  location.href = "/community/write";
};

const insert_meal_feed = (meal) => {
  // TODO: 페이지네이션 결과 삽입
  console.log('TODO: Pagination')
};

const get_next_meal = async (feed_id) => {
  xhr = new XMLHttpRequest();
  await xhr.open("GET", `/community/next?feed_id=${feed_id}`, true);
  await xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onload = () => {
    if (xhr.status === 200) {
      const meal = JSON.parse(xhr.responseText);
    } else {
      alert("잠시 후 다시 시도해주세요");
    }
  };
  await xhr.send();
};

window.onscroll = function () {
  if (
    window.innerHeight + Math.ceil(window.pageYOffset) >=
    document.body.offsetHeight
  ) {
    console.log('TODO: Pagination')
    // get_next_meal(27);
  }
};
